# Karmen Tsang — Portfolio Static Site

A static site generator from my Honours project during University.

#### It's not the best - I know 😭 

It ingests Markdown or raw HTML files from the `/content` folder, renders them with Jinja2 templates, and publishes the finished pages to `/docs`, ready for GitHub Pages.

> 💜 **Live site:** [https://karmentsang.github.io](https://karmentsang.github.io)

---

## ✨ Features

- **Markdown & HTML support** — write posts in either format. Markdown is rendered to HTML5 automatically.
- **YAML front‑matter** — control titles, descriptions, categories, dates, favourites, and more.
- **Jinja2 templates** — maintain consistent design via `templates/base.html`, `index.html`, etc.
- **Automatic homepage** — the build script compiles category listings, recent posts, and a favourites section.
- **Photo album generator** — `assets/includes/album.py` scans sub‑folders of images and creates `album.html` galleries.
- **Zero‑config deployment** — push to GitHub; everything in `/docs` is served at `<username>.github.io`.

#### Though I wanted a more dynamic and creative portfolio, therefore I have not used everything I've implemented and I've changed a few things to my liking.

---

## 📹 Project Layout

```
.
├── assets/                 # CSS, JS, images, additional files
├── content/                # Your posts (Markdown or HTML)
├── docs/                   # Generated site (auto‑created)
├── templates/              # Jinja2 templates (base, home, album, footer…)
├── build.py                # Static‑site build script
└── README.md               # You’re reading it
```

---

## 🚀 Quick Start

```bash
# 1 · Clone
$ git clone https://github.com/karmentsang/karmentsang.github.io
$ cd karmentsang.github.io

# 2 · Install dependencies (Python 3.9+)
$ python -m pip install markdown jinja2 pyyaml pillow
# – or –
$ python -m pip install -r requirements.txt

# 3 · Build the site
$ python build.py            # outputs to /docs
$ open docs/home.html         # preview locally

# 4 · Publish
$ git add . && git commit -m "Update site" && git push
# GitHub Pages will serve https://<user>.github.io automatically
```

---

## 📝Front‑Matter Reference

| Key           | Type    | Example          | Notes                                  |
| ------------- | ------- | ---------------- | -------------------------------------- |
| `title`       | string  | `"My Project"`   | Shown as `<h1>` & HTML `<title>`       |
| `description` | string  | `"Case study"`   | Meta description + hero copy           |
| `date`        | string  | `"2025-06-20"`   | ISO‑8601, used for sorting             |
| `author`      | string  | `"Karmen Tsang"` | Optional                               |
| `category`    | string  | `"Photography"`  | Groups posts on homepage               |
| `favourite`   | boolean | `true`           | Shows post in "Favourites" list        |
| `include`     | boolean | `false`          | Excludes page from listings when `false` |

---

## Adding an Album

1. Drop sub‑folders of images (jpg/png) into `assets/images/subs/<project>/`.
2. Run `python build.py` (which calls `album()` internally).
3. A new `docs/album.html` page will be generated featuring every folder & image.

---

##  Customising

- **Templates** — edit anything in `/templates`; they’re plain Jinja2 + HTML.
- **Styling** — global styles live in `assets/css/`.
- **Content** — add new Markdown/HTML files under `/content`; use front‑matter to control behaviour.

---

## 📄 License

MIT © 2025 Karmen Tsang. Feel free to fork & remix.

---

## 🙏 Acknowledgements

Built with [Python Markdown](https://python‑markdown.github.io/), [Jinja2](https://jinja.palletsprojects.com/), [Pillow](https://python‑pillow.org/) — and plenty of matcha. 🍵

