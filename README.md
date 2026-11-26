# Lodges of Round Table – static site

Plain HTML and one CSS file. No Drupal, no database, no build step, nothing to patch.

## Before switching off the old server

Download the images from the live Drupal site (one time only):

```bash
bash fetch-images.sh
```

This fills `images/` and adds `favicon.ico`. Commit those files.

## Publishing on GitHub Pages

1. Create a **public** repository (e.g. `lodgesofroundtable/website`) and push these files to `main`.
2. Repo **Settings → Pages**: Source = *Deploy from a branch*, Branch = `main`, folder = `/ (root)`.
3. The `CNAME` file already contains `www.lodgesofroundtable.uk`. At your DNS provider:
   - `www` → **CNAME** → `<your-github-username>.github.io`
   - apex `lodgesofroundtable.uk` → **A** records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
4. Once the certificate is issued, tick **Enforce HTTPS** in Settings → Pages.
5. Optional but recommended: verify the domain under your account/org *Settings → Pages → Verified domains*.

## Layout

| Path | What it is |
|---|---|
| `/` | Network home page |
| `/lodges/` | Lodge directory (edit the table in `lodges/index.html`) |
| `/cardiff-2026/` | Archive of the 2026 Reunion (overview, itinerary, accommodation, Cardiff guide) |
| `/contact-us/` | Email + address (the Drupal webform is replaced by a mailto link) |
| `itinerary/`, `accommodation/`, `cardiff/`, `form/book/`, `terms-and-conditions/` | Redirects from the old Drupal URLs |

## Adding a lodge

Open `lodges/index.html`, copy a `<tr>…</tr>` row and edit it. The search box filters automatically.

## Changing the menu or footer

The header and footer are repeated in every `index.html`. Use find-and-replace across the folder, or regenerate with `build.py` (kept in the repo's `_build/` folder; needs Python 3).
