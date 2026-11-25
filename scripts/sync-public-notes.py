#!/usr/bin/env python3
"""Copy the publish set from My-Vault into a Quartz content/ folder.

Publish set: public/, Computer Science/, Mathematics/,
Robot Learning Book/, and Robot Learning Literature/.

Notes stay in the vault. This script only copies into the Quartz repo.
Images already inside the publish set keep their relative paths.
Images embedded from outside (for example Screenshots/) are copied so
links still resolve: vault-root paths such as Screenshots/ go to
content/Screenshots/, and other outside embeds go to content/attachments/.

Note text is not rewritten, except for a markdown or wikilink image path
that would otherwise escape content/; those are pointed at the copied file.

Default is a dry run. Pass --apply to copy files.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

PUBLISH_FOLDERS = [
    "public",
    "Computer Science",
    "Mathematics",
    "Robot Learning Book",
    "Robot Learning Literature",
]

WIKI_LINK = re.compile(r"(?<!!)\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
WIKI_EMBED = re.compile(r"!\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
MD_IMAGE = re.compile(r"!\[[^\]]*\]\((?:<([^>]+)>|([^)\s]+))\)")

NOTE_EXTS = {".md", ".markdown", ".canvas", ".base"}
MEDIA_EXTS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",
    ".pdf",
    ".mp4",
    ".mov",
    ".webm",
    ".heic",
    ".avif",
    ".bmp",
    ".tif",
    ".tiff",
}
SKIP_EXTS = {".py", ".pyc", ".sh", ".ds_store"}
SKIP_DIR_NAMES = {".obsidian", "__pycache__"}
# Build tooling, not site content
SKIP_PATH_PREFIXES = [
    "Robot Learning Book/Tools/",
]
MAX_VIDEO_BYTES = 20 * 1024 * 1024
VIDEO_EXTS = {".mp4", ".mov", ".webm"}
MANAGED_DEST_FILES = {"index.md"}  # homepage lives in the Quartz repo


def parse_args() -> argparse.Namespace:
    default_vault = Path.home() / "My-Vault"
    default_dest = Path.home() / "Developer" / "kk-notes" / "content"
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--vault", type=Path, default=default_vault)
    p.add_argument("--dest", type=Path, default=default_dest)
    p.add_argument("--apply", action="store_true", help="Copy files. Default is dry run.")
    p.add_argument(
        "--prune",
        action="store_true",
        help="With --apply, remove previously synced files that are no longer in the publish set. Never deletes dest/index.md unless the vault has public/index.md.",
    )
    p.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Vault-relative note path to exclude (repeatable).",
    )
    return p.parse_args()


def rel_to(path: Path, root: Path) -> str | None:
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except ValueError:
        return None


def under_any(path: Path, roots: list[Path]) -> bool:
    for root in roots:
        try:
            path.resolve().relative_to(root.resolve())
            return True
        except ValueError:
            continue
    return False


def should_skip_dir(path: Path, vault: Path) -> str | None:
    rel = rel_to(path, vault) or ""
    for part in path.parts:
        if part in SKIP_DIR_NAMES:
            return f"skipped directory {part}"
    for prefix in SKIP_PATH_PREFIXES:
        if rel == prefix.rstrip("/") or rel.startswith(prefix):
            return f"skipped tooling path {prefix.rstrip('/')}"
    return None


def classify_source_file(path: Path, vault: Path) -> str | None:
    """Return a skip reason, or None if the file may be copied as publish-set content."""
    if path.name == ".DS_Store":
        return "skipped .DS_Store"
    reason = should_skip_dir(path.parent, vault)
    if reason:
        return reason
    ext = path.suffix.lower()
    if ext in SKIP_EXTS or path.name.lower() == ".ds_store":
        return f"skipped {ext or path.name} file"
    if ext in VIDEO_EXTS and path.stat().st_size > MAX_VIDEO_BYTES:
        mb = path.stat().st_size / (1024 * 1024)
        return f"skipped large video ({mb:.1f} MB)"
    # requirements.txt and similar tooling at repo roots of Tools already skipped
    if path.name.lower() == "requirements.txt" and "Tools" in path.parts:
        return "skipped tooling requirements.txt"
    return None


def iter_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*") if p.is_file())


def extract_wiki_and_embeds(text: str) -> tuple[list[str], list[str], list[str]]:
    wikis = [m.group(1).strip() for m in WIKI_LINK.finditer(text)]
    embeds = [m.group(1).strip() for m in WIKI_EMBED.finditer(text)]
    images = []
    for m in MD_IMAGE.finditer(text):
        raw = (m.group(1) or m.group(2) or "").strip()
        if raw.startswith(("http://", "https://", "data:")):
            continue
        images.append(raw.strip("'\""))
    return wikis, embeds, images


def normalize_target(target: str) -> str:
    return target.replace("%20", " ").strip().lstrip("/")


def resolve_in_vault(vault: Path, note: Path, target: str) -> Path | None:
    target = normalize_target(target)
    if not target:
        return None
    basename = Path(target).name
    candidates = [
        (note.parent / target).resolve(),
        (vault / target).resolve(),
        (vault / "Screenshots" / basename).resolve(),
        (note.parent / basename).resolve(),
    ]
    seen: set[Path] = set()
    for cand in candidates:
        if cand in seen:
            continue
        seen.add(cand)
        if rel_to(cand, vault) is None:
            continue
        if cand.is_file():
            return cand
    matches = [p for p in vault.rglob(basename) if p.is_file() and p.name == basename]
    if not matches:
        return None

    def rank(p: Path) -> tuple[int, str]:
        rel = str(p.relative_to(vault))
        if rel.startswith("public/") or any(
            rel == d or rel.startswith(d + "/") for d in PUBLISH_FOLDERS
        ):
            return (0, rel)
        if rel.startswith("Screenshots/"):
            return (1, rel)
        return (2, rel)

    return sorted(matches, key=rank)[0]


def dest_for_outside_embed(vault: Path, dest_root: Path, src: Path) -> Path:
    """Place an outside embed so typical vault-root and Screenshots links resolve."""
    rel = rel_to(src, vault)
    if rel and rel.startswith("Screenshots/"):
        return dest_root / rel
    return dest_root / "attachments" / src.name


def main() -> int:
    args = parse_args()
    vault = args.vault.expanduser().resolve()
    dest = args.dest.expanduser().resolve()
    excludes = {str(Path(x)) for x in args.exclude}

    if not vault.is_dir():
        print(f"error: vault not found: {vault}", file=sys.stderr)
        return 1
    try:
        dest.relative_to(vault)
        print("error: destination must be outside the vault", file=sys.stderr)
        return 1
    except ValueError:
        pass

    publish_roots = []
    missing_folders = []
    for name in PUBLISH_FOLDERS:
        root = vault / name
        if root.is_dir():
            publish_roots.append(root)
        else:
            missing_folders.append(name)

    copies: list[tuple[Path, Path, str]] = []
    skipped: list[tuple[str, str]] = []
    excluded: list[str] = []
    missing_embeds: list[tuple[str, str]] = []

    for root in publish_roots:
        for src in iter_files(root):
            rel = rel_to(src, vault) or str(src)
            if rel in excludes:
                excluded.append(rel)
                skipped.append((rel, "excluded by --exclude"))
                continue
            reason = classify_source_file(src, vault)
            if reason:
                skipped.append((rel, reason))
                continue
            copies.append((src, dest / Path(rel), "publish"))

    # Parse notes in the publish set for embeds
    note_files = [src for src, _, kind in copies if src.suffix.lower() in NOTE_EXTS]
    for src in note_files:
        try:
            text = src.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"warning: could not read {src} as text, skipping embed scan")
            continue
        _, embeds, images = extract_wiki_and_embeds(text)
        for target in embeds + images:
            resolved = resolve_in_vault(vault, src, target)
            if resolved is None:
                missing_embeds.append((rel_to(src, vault) or str(src), target))
                continue
            if under_any(resolved, publish_roots):
                # already copied with folder structure, unless it was skipped
                continue
            out = dest_for_outside_embed(vault, dest, resolved)
            # collision: same dest, different source
            clash = [c for c in copies if c[1] == out and c[0].resolve() != resolved.resolve()]
            if clash:
                skipped.append(
                    (
                        rel_to(resolved, vault) or str(resolved),
                        f"filename collision at {out.relative_to(dest)}",
                    )
                )
                continue
            copies.append((resolved, out, "embed"))

    uniq: list[tuple[Path, Path, str]] = []
    seen: set[tuple[Path, Path]] = set()
    for src, out, kind in copies:
        key = (src.resolve(), out)
        if key in seen:
            continue
        seen.add(key)
        uniq.append((src, out, kind))

    mode = "APPLY" if args.apply else "DRY RUN"
    print(f"{mode}")
    print(f"vault: {vault}")
    print(f"dest:  {dest}")
    if missing_folders:
        print("missing publish folders:", ", ".join(missing_folders))
    print()
    print(f"copy {len(uniq)} file(s)")
    for src, out, kind in uniq:
        via = rel_to(src, vault) or str(src)
        print(f"  [{kind:7}] {via}  ->  {out.relative_to(dest)}")

    if skipped:
        print(f"\nskipped {len(skipped)} file(s):")
        for rel, reason in skipped:
            print(f"  {rel}  ({reason})")
    if excluded:
        print(f"\nexcluded notes: {len(excluded)}")
        for rel in excluded:
            print(f"  {rel}")
    if missing_embeds:
        print(f"\nmissing embeds: {len(missing_embeds)}")
        for note, target in missing_embeds:
            print(f"  {note}: {target}")

    if not args.apply:
        print("\nNo files written. Re-run with --apply to copy.")
        return 0

    dest.mkdir(parents=True, exist_ok=True)
    for src, out, kind in uniq:
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, out)

    if args.prune:
        expected = {out.resolve() for _, out, _ in uniq}
        public_has_index = (vault / "public" / "index.md").is_file()
        index = (dest / "index.md").resolve()
        removed = 0
        if dest.exists():
            for path in dest.rglob("*"):
                if not path.is_file() or path.name == ".DS_Store":
                    continue
                if path.resolve() in expected:
                    continue
                if path.resolve() == index and not public_has_index:
                    continue
                if path.name in MANAGED_DEST_FILES and path.parent == dest and not public_has_index:
                    continue
                path.unlink()
                removed += 1
                print(f"pruned {path}")
        print(f"pruned {removed} file(s)")

    print("done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
