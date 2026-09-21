# RecLora account-test mirror

This repository is a separate copy of the current `rectest` mirror. It keeps the mirrored route structure and major pages while adding a compact RecLora rebrand layer.

## What changed

- The existing mirrored HTML route set is preserved.
- `reclora-theme.css` is loaded across the mirrored pages so colors and shared branding can be changed in one file.
- The supplied logo is stored at `logos/reclora/Reclora logo.png` and is used in the shared RecLora brand bar.
- A **Test accounts** link is added to mirrored pages.
- `account-test/` provides local browser-only signup, login, logout, and profile editing.

## Test accounts

Open `account-test/` or use the **Test accounts** link on any mirrored page. These are deliberately local demo accounts:

- They are stored in the browser's `localStorage`.
- They are not connected to Rec Room, OAuth, billing, or any real account system.
- Passwords are only for local testing and must not be reused anywhere.
- They do not create accounts on a server and are not suitable for production authentication.

This keeps the static GitHub Pages mirror safe while letting you test account screens and profile states.

## Easy editing

- Change the global RecLora colors, spacing, and shared account UI in `reclora-theme.css`.
- Replace the logo at `logos/reclora/Reclora logo.png`.
- Re-run `python3 tools/rebrand_reclora.py` after adding newly mirrored HTML pages.
- The original mirrored content pages remain individual exported HTML files so their page-specific content and images remain available.

## Preview

```bash
python3 -m http.server 4175
```

Then open `http://localhost:4175/`. The account-test flow requires a browser because it uses `localStorage`.
