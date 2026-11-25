# Syncing notes from My-Vault

Notes stay in the private vault. This repo only receives a copy of the publish set.

## Publish set

These vault folders are copied into `content/`, keeping their folder names:

- `public/`
- `Computer Science/`
- `Mathematics/`
- `Robot Learning Book/`
- `Robot Learning Literature/`

The site homepage is `content/index.md` in this repo, not a vault note.

## Paths

- Vault: `/Users/kazybekkhairulla/My-Vault`
- Quartz repo: `/Users/kazybekkhairulla/Developer/kk-notes`
- Site content: `/Users/kazybekkhairulla/Developer/kk-notes/content/`

## Script

`scripts/sync-public-notes.py` copies the publish set into `content/`. Images already inside those folders keep their relative paths. Image embeds (`![[...]]` and `![](...)`) that live outside the publish set (for example in `Screenshots/`) are copied so links resolve: `Screenshots/` files go to `content/Screenshots/`, and other outside files go to `content/attachments/`.

The script skips `.py`, `.pyc`, `.sh`, `.obsidian`, `__pycache__`, `Robot Learning Book/Tools/`, and videos larger than 20 MB.

Dry run (default, writes nothing):

```bash
python3 scripts/sync-public-notes.py \
  --vault /Users/kazybekkhairulla/My-Vault \
  --dest /Users/kazybekkhairulla/Developer/kk-notes/content
```

Copy files:

```bash
python3 scripts/sync-public-notes.py --apply
```

`--prune` (only with `--apply`) deletes previously synced files that are no longer in the publish set. It will not delete `content/index.md` unless `public/index.md` exists.

`--exclude path/from/vault/Note.md` leaves a specific note out of the copy.

## How to publish a note

1. Put it in one of the publish-set folders in My-Vault, or add a new folder to the script's `PUBLISH_FOLDERS` list after confirming it is safe to publish.
2. Run the script with `--apply`.
3. In `kk-notes`, commit and push branch `v5`, or deploy with wrangler until Git is connected.

Do not move notes around in the vault just to publish them; that would break Obsidian links.

## How to unpublish a note

1. Remove it from the publish set, or pass `--exclude`.
2. Run the script with `--apply --prune`.
3. Commit and push `v5`.

## Safety

- Never make `My-Vault` public, and never commit or push My-Vault from this workflow.
- Keep Obsidian Git pointed at My-Vault, not at `kk-notes`.
- Do not commit secrets into this repo.
