# Syncing notes from My-Vault

Only notes inside the vault folder `public/` are published. Private notes never enter this repo.

## Paths

- Vault: `/Users/kazybekkhairulla/My-Vault`
- Publish folder: `/Users/kazybekkhairulla/My-Vault/public/`
- Quartz repo: `/Users/kazybekkhairulla/Developer/kk-notes`
- Site content: `/Users/kazybekkhairulla/Developer/kk-notes/content/`

## Script

`scripts/sync-public-notes.py` copies everything under `My-Vault/public/` into `kk-notes/content/`, keeping relative paths. It also scans those public notes for image embeds (`![[...]]` and `![](...)`), resolves them from the note folder, vault `Screenshots/`, or elsewhere in the vault, and copies those files into `content/attachments/` under their original filename. Note text is not rewritten.

Quartz is configured with shortest link resolution, so `![[photo.png]]` still works after the image moves to `attachments/`. Markdown links that point at a path outside `public/` (for example `![](../Screenshots/photo.png)`) are left unchanged and may break; prefer wikilinks, or keep the image inside `public/`.

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

`--prune` (only with `--apply`) deletes previously synced files that are no longer in `public/`. It will not delete `content/index.md` unless `public/index.md` exists.

## How to publish a note

1. Put the note in `My-Vault/public/` (do not leave private notes there).
2. Keep any images it embeds in the vault so the script can find them. Prefer putting those images in `public/` as well, or leave them in `Screenshots/`.
3. Run the script with `--apply`.
4. In `kk-notes`, commit and push branch `v5`. Cloudflare Pages will rebuild when Git is connected.

## How to unpublish a note

1. Remove it from `My-Vault/public/`.
2. Run the script with `--apply --prune`.
3. Commit and push `v5`.

## Quartz Syncer (optional, recommended later)

The [Quartz Syncer](https://github.com/saberzero1/quartz-syncer) Obsidian plugin can publish only a chosen folder to this repo's `content/` folder on a desktop timer, so editing a public note is the only manual writing step. Install it if you want auto-publish from Obsidian. Until then, use the script after you add or remove notes in `public/`. Obsidian Git should keep pointing at the private `My-Vault` repo, not at `kk-notes`.

## Safety

- Never make `My-Vault` public.
- Never run this script against folders other than `public/` for Markdown.
- Do not commit secrets into this repo.
