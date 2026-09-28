# BG Remover

Remove image backgrounds instantly — entirely in your browser. No server, no uploads, fully private.

## How It Works

Uses [@imgly/background-removal](https://github.com/nicbarker/imgly-background-removal) which runs an ML model (ONNX) directly in the browser via WebAssembly. Your images never leave your device.

## Deploy on GitHub Pages

1. Push this repo to GitHub
2. Go to **Settings → Pages**
3. Under **Source**, select **Deploy from a branch**
4. Choose `main` branch and `/ (root)` folder
5. Click **Save** — your site will be live at `https://<username>.github.io/<repo-name>/`

## Project Structure

```
BG-remover/
├── index.html    # The entire app (HTML + CSS + JS)
├── .gitignore
└── README.md
```

## License

MIT
