# Angaza Tumaini — Project Documentation

This repository contains the static website for Angaza Tumaini Mission Center. Below is an overview of the project, development timeline, deployment, and billing information.

## Project Overview
- Static site composed of `index.html`, `contact.html`, and `newsletter.html`.
- Built with HTML, Tailwind CSS (via CDN), and small client-side JS. Local images and png icons are in `filez/` and `filez/icons/`.

## Development Timeline
- Initial scaffolding of static pages and assets.
- Added footer social icons; switched to local PNG icons for consistent rendering.
- Created `newsletter.html` and wired newsletter CTA in the footer.
- Updated contact details (email: AngazaTumaini.org@gmail.com, phone: +254 716 475764, WhatsApp: https://wa.link/xjt1s4).
- Added mailto fallback logic to open Gmail compose if native mail client doesn't respond.
- Deployed to Vercel; pushed repository to GitHub: `https://github.com/alvingavi0/Angaza-Tumaini`.

## Files of note
- `index.html` — main homepage; updated footer, icons, mailto fallback; header restored.
- `contact.html` — contact page with form (Formspree) and mailto fallback.
- `newsletter.html` — newsletter & socials page.
- `filez/icons/` — local PNG icons in use: `facebook.png`, `Instagram.png`, `Gmail.png`, `tiktok.png`, `Whatsapp.png`.

## How to preview locally
Run a static server in the project root (example):

```powershell
python -m http.server 8000
```
Open `http://127.0.0.1:8000/index.html` in your browser.

## Deployment
- Vercel: previously deployed with `npx vercel --prod`. If CLI rate limits occur, connect the GitHub repo in the Vercel dashboard to enable auto-deploy by push.

## Billing
- Service: Web development and deployment for Angaza Tumaini Mission Center
- Amount: 21,000 shillings
- Payment via phone number: `0759106034`

## Screenshots
Insert screenshots of pages into the Word document `Angaza-Tumaini-Documentation.docx` or add them here as needed.

---

If you want any formatting changes to the Word document or additional sections (asset inventory, accessibility checklist, or CI/CD instructions), tell me and I'll update both the `.docx` and `README.md` accordingly.
