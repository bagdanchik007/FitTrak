# Download / install GUI

## On the website
- **App installieren** — uses the browser PWA prompt when available
- **Release / ZIP herunterladen** — opens GitHub Releases (source + assets)

## Configure URL
Set in `frontend/.env`:

```env
VITE_APP_DOWNLOAD_URL=https://github.com/bagdanchik007/FitTrak/releases/latest
```

## Note
This is a web app + PWA, not a separate Windows `.exe`. Phone: Add to Home Screen. Laptop: install PWA in Chrome/Edge or use the site.
