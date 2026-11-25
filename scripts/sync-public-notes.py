#!/usr/bin/env python3
"""Copy only My-Vault/public notes (plus embedded images) into a Quartz content/ folder.

By default this is a dry run. Pass --apply to copy files.
Never copies Markdown from outside public/. Referenced images may be
resolved from Screenshots/ or elsewhere in the vault, and are written
to content/attachments/ under their basename. Note contents are not rewritten.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

WIKI_EMBED = re.compile(r"!\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
# Markdown images: ![alt](path) or ![alt](<path with spaces>)
MD_IMAGE = re.compile(r"!\[[^\]]*\]\((?:<([^>]+)>|([^)\s]+))\)")

IMAGE_EXTS = {
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

NOTE_EXTS = {".md", ".markdown", ".canvas", ".base"}


def parse_args() -> argparse.Namespace:
    default_vault = Path.home() / "My-Vault"
    default_dest = Path.home() / "Developer" / "kk-notes" / "content"
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--vault", type=Path, default=default_vault, help="Path to the Obsidian vault")
    p.add_argument("--dest", type=Path, default=default_dest, help="Quartz content/ directory")
    p.add_argument("--apply", action="store_true", help="Copy files. Default is dry run.")
    p.add_argument(
        "--prune",
        action="store_true",
        help="With --apply, remove previously synced files that are no longer in public/ (never deletes dest/index.md unless public/ has index.md)",
    )
    return p.parse_args()


def rel_or_none(path: Path, root: Path) -> str | None:
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except ValueError:
        return None


def iter_public_files(public: Path) -> list[Path]:
    files = [p for p in public.rglob("*") if p.is_file() and p.name != ".DS_Store"]
    return sorted(files)


def extract_embed_targets(text: str) -> list[str]:
    found: list[str] = []
    for m in WIKI_EMBED.finditer(text):
        found.append(m.group(1).strip())
    for m in MD_IMAGE.finditer(text):
        raw = (m.group(1) or m.group(2) or "").strip()
        # strip optional title: path "title"
        if raw.startswith(("http://", "https://", "data:")):
            continue
        found.append(raw.strip("'\""))
    return found


def resolve_embed(vault: Path, note: Path, target: str) -> Path | None:
    # Unescape simple Obsidian/markdown paths
    target = target.replace("%20", " ").strip().lstrip("/")
    if not target:
        return None
    candidates: list[Path] = []
    # relative to the note
    candidates.append((note.parent / target).resolve())
    # path from vault root
    candidates.append((vault / target).resolve())
    # common attachment folder + basename
    basename = Path(target).name
    candidates.append((vault / "Screenshots" / basename).resolve())
    candidates.append((vault / "public" / basename).resolve())
    candidates.append((note.parent / basename).resolve())

    seen: set[Path] = set()
    for cand in candidates:
        if cand in seen:
            continue
        seen.add(cand)
        try:
            cand.relative_to(vault.resolve())
        except ValueError:
            continue
        if cand.is_file():
            return cand

    # Filename search across the vault (referenced attachments only)
    matches = [p for p in vault.rglob(basename) if p.is_file() and p.name == basename]
    # Prefer files under public/ or Screenshots/
    def rank(p: Path) -> tuple[int, str]:
        rel = str(p.relative_to(vault))
        if rel.startswith("public/") or rel.startswith("public\\"):
            return (0, rel)
        if rel.startswith("Screenshots/") or rel.startswith("Screenshots\\"):
            return (1, rel)
        return (2, rel)

    matches = sorted(matches, key=rank)
    if not matches:
        return None
    return matches[0]


def is_note(path: Path) -> bool:
    return path.suffix.lower() in NOTE_EXTS


def main() -> int:
    args = parse_args()
    vault = args.vault.expanduser().resolve()
    dest = args.dest.expanduser().resolve()
    public = vault / "public"

    if not vault.is_dir():
        print(f"error: vault not found: {vault}", file=sys.stderr)
        return 1
    if not public.is_dir():
        print(f"error: public/ folder not found: {public}", file=sys.stderr)
        return 1
    if dest == vault or vault in dest.parents and dest == public:
        print("error: destination must not be the vault itself", file=sys.stderr)
        return 1
    # Safety: never use a dest inside the vault except we allow nothing under vault
    try:
        dest.relative_to(vault)
        print("error: destination must be outside the vault (use the Quartz content/ folder)", file=sys.stderr)
        return 1
    except ValueError:
        pass

    public_files = iter_public_files(public)
    copies: list[tuple[Path, Path, str]] = []  # src, dest, kind
    missing: list[tuple[Path, str]] = []
    ambiguous: list[tuple[str, list[str]]] = []

    for src in public_files:
        rel = src.relative_to(public)
        copies.append((src, dest / rel, "public"))

    # Parse notes under public/ only
    for src in public_files:
        if not is_note(src):
            continue
        try:
            text = src.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"warning: could not read {src} as text, skipping embed scan")
            continue
        for target in extract_embed_targets(text):
            resolved = resolve_embed(vault, src, target)
            if resolved is None:
                missing.append((src, target))
                continue
            # If the file already lives under public/, it is copied with its
            # relative path above. Still also copy embeds from outside public/
            # into attachments/.
            try:
                resolved.relative_to(public.resolve())
                # already included as a public/ copy
                continue
            except ValueError:
                pass
            suffix = resolved.suffix.lower()
            if suffix not in IMAGE_EXTS and suffix not in NOTE_EXTS:
                # still copy if it was explicitly embedded
                pass
            out = dest / "attachments" / resolved.name
            # collision check
            existing = [c for c in copies if c[1] == out and c[0].resolve() != resolved.resolve()]
            if existing:
                ambiguous.append((resolved.name, [str(existing[0][0]), str(resolved)]))
                continue
            copies.append((resolved, out, "embed"))

    # Deduplicate exact src->dest
    uniq: list[tuple[Path, Path, str]] = []
    seen_pair: set[tuple[Path, Path]] = set()
    for src, out, kind in copies:
        key = (src.resolve(), out)
        if key in seen_pair:
            continue
        seen_pair.add(key)
        uniq.append((src, out, kind))

    mode = "APPLY" if args.apply else "DRY RUN"
    print(f"{mode}")
    print(f"vault:  {vault}")
    print(f"public: {public}")
    print(f"dest:   {dest}")
    print()
    if not uniq:
        print("nothing to copy")
    for src, out, kind in uniq:
        via = rel_or_none(src, vault) or str(src)
        print(f"  [{kind:7}] {via}  ->  {out}")

    if missing:
        print("\nmissing embeds:")
        for note, target in missing:
            rel = rel_or_none(note, vault) or str(note)
            print(f"  {rel}: {target}")
    if ambiguous:
        print("\nfilename collisions in content/attachments/ (not copied):")
        for name, paths in ambiguous:
            print(f"  {name}:")
            for p in paths:
                print(f"    {p}")

    if not args.apply:
        print("\nNo files written. Re-run with --apply to copy.")
        return 0 if not ambiguous else 2

    dest.mkdir(parents=True, exist_ok=True)
    (dest / "attachments").mkdir(parents=True, exist_ok=True)
    for src, out, kind in uniq:
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, out)
        print(f"copied {out}")

    if args.prune:
        # Track expected outputs from this run, plus dest/index.md if not in public/
        expected = {out.resolve() for _, out, _ in uniq}
        public_has_index = (public / "index.md").is_file()
        index = (dest / "index.md").resolve()
        removed = 0
        if dest.exists():
            for path in dest.rglob("*"):
                if not path.is_file():
                    continue
                if path.name == ".DS_Store":
                    continue
                if path.resolve() in expected:
                    continue
                if path.resolve() == index and not public_has_index:
                    continue
                path.unlink()
                removed += 1
                print(f"pruned {path}")
        print(f"pruned {removed} file(s)")

    print("done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
