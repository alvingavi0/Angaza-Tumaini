from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from datetime import datetime

# Create PDF
pdf_file = '../Angaza-Tumaini-Documentation.pdf'
doc = SimpleDocTemplate(pdf_file, pagesize=letter,
                        rightMargin=0.75*inch, leftMargin=0.75*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)

# Styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=16,
    textColor='#1D4ED8',
    spaceAfter=12,
    alignment=TA_CENTER
)
heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=12,
    textColor='#1D4ED8',
    spaceAfter=8,
    spaceBefore=8
)
body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontSize=10,
    spaceAfter=6
)

# Content
story = []

# Title
story.append(Paragraph('Angaza Tumaini Mission Center — Project Documentation', title_style))
story.append(Spacer(1, 0.2*inch))

# Project Overview
story.append(Paragraph('1. Project Overview', heading_style))
story.append(Paragraph('Angaza Tumaini is a static website built with plain HTML, Tailwind CSS (via CDN), and small client-side JavaScript. The site includes pages: index.html (home), contact.html (contact), newsletter.html (newsletter &amp; socials). Local image assets and PNG icons live in the folder filez/ and filez/icons/.', body_style))
story.append(Spacer(1, 0.1*inch))

# Timeline
story.append(Paragraph('2. Development timeline (Beginning → End)', heading_style))
timeline_items = [
    'Initial scaffolding: Static HTML pages for Home, Contact, and supporting assets. Tailwind loaded from CDN and Lucide icons used for vector icons initially.',
    'Iterative updates: Footer social icons were added and changed from inline/SVG to local PNG files to ensure consistent rendering on user systems.',
    'Newsletter page: Created newsletter.html and wired an in-site CTA that navigates from footer button to this page.',
    'Contact updates: Mailto and tel links set to AngazaTumaini.org@gmail.com and tel:+254716475764, WhatsApp short link https://wa.link/xjt1s4 added.',
    'Mailto fallback: Small JS heuristic added to open Gmail compose if mailto doesn\'t open a native client.',
    'Visual/UX fixes: Circular PNG icons for social links, header/nav restored to original layout after accidental change.',
    'Deployment: Deployed to Vercel using the CLI. Repository was committed and pushed to GitHub. Cleaned up unused SVG icon files from filez/icons/ and pushed the cleanup commit.'
]
for item in timeline_items:
    story.append(Paragraph('• ' + item, body_style))
story.append(Spacer(1, 0.1*inch))

# Files changed
story.append(Paragraph('3. Files changed / created', heading_style))
files_items = [
    'index.html: Footer icons, mailto/tel links, mailto fallback script, header restored, WhatsApp icon added.',
    'contact.html: Updated contact email, phone, and WhatsApp link; contact form using Formspree with mailto fallback.',
    'newsletter.html: New page created listing social channels and a mailto subscribe link.',
    'filez/icons/: PNG icons added (facebook.png, Instagram.png, Gmail.png, tiktok.png, Whatsapp.png). Unused SVGs removed.'
]
for item in files_items:
    story.append(Paragraph('• ' + item, body_style))
story.append(Spacer(1, 0.1*inch))

# Local preview
story.append(Paragraph('4. How to preview locally', heading_style))
story.append(Paragraph('Open a terminal in the project root and run a simple static server. Example using Python 3:', body_style))
story.append(Paragraph('<b>python -m http.server 8000</b>', body_style))
story.append(Paragraph('Then open http://127.0.0.1:8000/index.html in your browser to view the site.', body_style))
story.append(Spacer(1, 0.1*inch))

# Deployment
story.append(Paragraph('5. Deployment', heading_style))
story.append(Paragraph('Vercel: Deployed via <b>npx vercel --prod</b> from project root. If CLI rate limits occur, connect the GitHub repo in the Vercel dashboard to enable Git-based auto-deploy on push.', body_style))
story.append(Spacer(1, 0.1*inch))

# Screenshots
story.append(Paragraph('6. Screenshots (placeholders)', heading_style))
story.append(Paragraph('<b>Page: index.html</b>', body_style))
story.append(Paragraph('[Insert screenshot of index.html here]', body_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph('<b>Page: contact.html</b>', body_style))
story.append(Paragraph('[Insert screenshot of contact.html here]', body_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph('<b>Page: newsletter.html</b>', body_style))
story.append(Paragraph('[Insert screenshot of newsletter.html here]', body_style))
story.append(Spacer(1, 0.2*inch))

# Billing
story.append(PageBreak())
story.append(Paragraph('7. Billing', heading_style))
story.append(Paragraph('<b>Service:</b> Web development and deployment for Angaza Tumaini Mission Center', body_style))
story.append(Paragraph('<b>Amount:</b> 21,000 shillings', body_style))
story.append(Paragraph('<b>Payment via phone number:</b> 0759106034', body_style))
story.append(Spacer(1, 0.2*inch))

# Notes
story.append(Paragraph('8. Notes &amp; Next steps', heading_style))
story.append(Paragraph('• Verify live site on Vercel and test mailto/tel/WhatsApp links on target devices. Provide screenshots and any requested copy changes and I will update and redeploy.', body_style))
story.append(Paragraph('• Optional: wire the newsletter subscription to a mailing provider (Mailchimp, ConvertKit, MailerLite) or add a server-side endpoint to collect emails.', body_style))
story.append(Spacer(1, 0.2*inch))

story.append(Paragraph('Generated: ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'), body_style))

# Build PDF
doc.build(story)
print(f'Saved {pdf_file}')
