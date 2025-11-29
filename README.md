# Angaza Tumaini Mission Center — Website Repository

This repository contains the complete static website for **Angaza Tumaini Mission Center**, a Christian community-based ministry serving children, families, and youth in Kibera, Nairobi, Kenya.

## 📋 Project Overview

**Organization:** Angaza Tumaini Mission Center  
**Tagline:** Shining the Hope of Christ through practical programs  
**Location:** Olympic Estate, Kibera, Nairobi, Kenya  
**Website Launch:** October 11, 2025  
**Live URL:** https://angaza-tumaini-o4nwg3zz9-calvin-wanyamas-projects.vercel.app

### Core Programs
1. **FAITH Program** — Spiritual formation and discipleship
2. **Education Program** — Academic tutoring and literacy support
3. **Life-Skills Program** — Communication, leadership, financial literacy training
4. **Socio-Economic Empowerment** — Vocational training and entrepreneurship
5. **Community Outreach** — Practical service, food drives, health campaigns, medical care

## 🏗️ Technical Stack

- **Frontend:** HTML5, CSS3, Tailwind CSS (CDN)
- **Styling:** Custom CSS with modern color scheme (Blue #1D4ED8, Green #10B981, Gold #FBBF24)
- **Icons:** Lucide Icons + local PNG files
- **Fonts:** Poppins (headings), Inter (body)
- **Form Backend:** Formspree
- **Hosting:** Vercel (auto-deploy from GitHub)
- **Version Control:** GitHub at https://github.com/alvingavi0/Angaza-Tumaini

## 📁 Repository Structure

```
Angaza-Tumaini/
├── index.html                          # Main homepage
├── contact.html                        # Contact page
├── newsletter.html                     # Newsletter & social media
├── README.md                           # This file
├── vercel.json                         # Vercel deployment config
├── scripts/
│   ├── generate_pdf.py                # Professional PDF documentation generator
│   ├── generate_docx.py               # Word document generator (reference)
│   └── generate_user_manual.py        # Comprehensive user manual generator
├── filez/
│   ├── logo/
│   │   ├── contact-logo.jpg           # Organization logo
│   │   └── favicon.ico                # Website favicon
│   ├── icons/
│   │   ├── facebook.png               # Social media icons
│   │   ├── Instagram.png
│   │   ├── Gmail.png
│   │   ├── tiktok.png
│   │   └── Whatsapp.png
│   ├── [Project photos]               # Community photography
│   │   ├── 6-2.jpg, 6-13.jpg, 6-16.jpg, 6-22.jpg, 6-32.jpg
│   │   ├── eric-and-krista.jfif      # Founders
│   │   ├── hypeman.jpg               # Evans Wandera
│   │   ├── Jackline.jpg              # Jackline Mueni
│   │   ├── Felix.jpeg                # Felix Mito
│   │   ├── Naureen.jpeg              # Naureen Mugeni
│   │   └── Ben.jpeg                  # Benard Owira
│   └── contact.jfif
├── Angaza-Tumaini-Documentation.pdf    # Professional invoice & project summary
└── Angaza-Tumaini-Website-User-Manual.pdf # Comprehensive user manual (NEW)
```

## 📄 Documentation Files

### 1. **Angaza-Tumaini-Website-User-Manual.pdf** (NEW - November 29, 2025)
**Comprehensive User Manual** with 10 major sections:
- About Angaza Tumaini Mission Center
- Founders & Leadership Team (with detailed bios)
- Mission, Vision & Core Values
- Our Five Core Programs (detailed descriptions)
- Website Overview & Navigation
- Page-by-page guide (Home, Contact, Newsletter)
- Contact & Support Information
- Frequently Asked Questions (FAQ)
- Ways to Support & Get Involved
- Technical Details & Accessibility Features

**Style:** Modern & Classic with professional typography, color scheme, and easy-to-follow layout
**Pages:** ~20+ pages of detailed information

### 2. **Angaza-Tumaini-Documentation.pdf**
Professional invoice-style documentation with:
- Project timeline (7 development phases)
- File inventory and structure
- Deployment information
- Itemized services breakdown (KES 15K dev + KES 4K deployment + KES 2K docs = KES 21K)
- Payment instructions and billing details
- Terms & conditions with checkmarks

### 3. **README.md**
This file — project overview, structure, and quick reference

## 🌐 Pages Overview

### Home Page (`index.html`)
- Hero section with rotating background images
- About Us section with organization tagline and team profiles
- Our Programs section (5 program cards + donate card)
- Our Impact in Numbers (animated counters)
- Get Involved section (multiple ways to support)
- Contact form (Formspree integrated)
- Footer with social media icons and newsletter CTA

**Key Features:**
- Sticky navigation header
- Mobile-responsive design
- Smooth scroll anchors
- Professional color scheme
- Team member cards with photos and bios

### Contact Page (`contact.html`)
- Contact form with email backend
- Direct contact channels:
  - Email: AngazaTumaini.org@gmail.com
  - Phone: +254 716 475764
  - WhatsApp: https://wa.link/xjt1s4
  - Address: Olympic Estate, Kibera, Nairobi
- Social media links
- Glass-effect card design

### Newsletter Page (`newsletter.html`)
- Newsletter subscription form
- Follow Us section (social media icons)
- Share buttons for content distribution
- Links to all major social channels

## 👥 Leadership Team

1. **Erick & Krista Baraza** — Founders & Missionaries
2. **Evans Wandera** — Programs Coordinator
3. **Jackline Mueni (Jay)** — Administrator & Programs Manager
4. **Felix Mito (Teacher Feloh)** — Tutor & Teacher
5. **Naureen Mugeni (Chief Chef)** — Cook
6. **Benard Owira (Benah)** — Support Staff

## 📞 Contact Information

- **Email:** AngazaTumaini.org@gmail.com
- **Phone:** +254 716 475764
- **WhatsApp:** https://wa.link/xjt1s4
- **Facebook:** https://www.facebook.com/profile.php?id=61552268876833
- **Address:** Olympic Estate, Kibera, Nairobi, Kenya
- **Website:** https://angaza-tumaini-o4nwg3zz9-calvin-wanyamas-projects.vercel.app

## 🚀 Local Development

### Prerequisites
- Python 3.11+ (for documentation generation)
- Modern web browser
- Optional: `reportlab` and `python-docx` for document generation

### Quick Start
1. Clone the repository:
   ```bash
   git clone https://github.com/alvingavi0/Angaza-Tumaini.git
   cd Angaza-Tumaini
   ```

2. Run a local server:
   ```powershell
   python -m http.server 8000
   ```

3. Open in browser:
   ```
   http://localhost:8000
   ```

### Generate Documentation
```powershell
# Generate professional invoice PDF
python scripts/generate_pdf.py

# Generate comprehensive user manual
python scripts/generate_user_manual.py
```

## 🌐 Deployment

**Hosting:** Vercel (https://vercel.com)
- Auto-deploy from GitHub on push to `main` branch
- Domain configured for custom URL support
- CDN and edge caching enabled

**Deployment Commands:**
```bash
# One-time Vercel setup
npx vercel --prod

# Subsequent updates (via GitHub)
git push origin main  # Auto-deploys via Vercel
```

## 💳 Billing & Services

**Service:** Website Development & Deployment for Angaza Tumaini Mission Center  
**Date:** October 11, 2025  
**Amount:** **KES 21,000**

**Service Breakdown:**
- Web Development (HTML, CSS, JavaScript): KES 15,000
- Deployment & Git Integration (Vercel): KES 4,000
- Documentation & Support Materials: KES 2,000

**Payment Method:** Mobile Money / Phone Transfer  
**Payment Phone:** 0759106034  
**Reference:** Angaza-Tumaini-2025-Oct

## 🎨 Design System

### Color Palette
- **Primary Blue:** #1D4ED8 (Trust, stability, spirituality)
- **Secondary Green:** #10B981 (Growth, life, hope)
- **Accent Gold:** #FBBF24 (Hope, inspiration, warmth)
- **Dark Charcoal:** #1F2937 (Text, sophistication)
- **Light Gray:** #F3F4F6 (Backgrounds, subtle accents)

### Typography
- **Headings:** Poppins (bold, modern)
- **Body:** Inter (clean, readable)
- **Font Sizes:** Responsive to device size

## ✅ Features & Highlights

✨ **Modern & Professional Design**  
📱 **Fully Responsive** (mobile, tablet, desktop)  
⚡ **Fast Loading** (optimized images and code)  
♿ **Accessible** (WCAG standards compliant)  
🔍 **SEO Optimized** (meta tags, structured content)  
📧 **Email Integration** (Formspree form backend)  
🔗 **Social Media Ready** (shareable content, social icons)  
📊 **Impact Metrics** (animated counters for statistics)  
🎯 **Clear CTAs** (donation, volunteering, newsletter signup)  

## 📖 How to Use the Manuals

1. **For website visitors:** Share the **User Manual PDF** to help people understand all pages and how to navigate
2. **For project stakeholders:** Share the **Documentation PDF** for billing, timeline, and services summary
3. **For developers:** Refer to this **README.md** for technical structure and deployment info

## 🔄 Version Control

**GitHub Repository:** https://github.com/alvingavi0/Angaza-Tumaini  
**Main Branch:** Contains production-ready code  
**Commit History:** Complete development timeline  

**Latest Commits:**
- e120f13: Add comprehensive User Manual with full website guide, team profiles, and FAQ
- 9d558c2: Enhance modern, professional PDF with improved styling, colors, and invoice formatting
- 0d56e1e: PDF alternative to .docx

## 📝 License & Attribution

**Organization:** Angaza Tumaini Mission Center  
**Founded:** By Erick and Krista Baraza  
**Website Created:** October 11, 2025  
**Maintained by:** Development team at Calvin Wanyama's Projects  

All content, images, and materials are the property of Angaza Tumaini Mission Center unless otherwise attributed.

---

**Last Updated:** November 29, 2025  
**For questions or updates, contact:** AngazaTumaini.org@gmail.com | +254 716 475764
 
