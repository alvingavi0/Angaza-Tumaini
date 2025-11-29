from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfgen import canvas
from datetime import datetime

# Create PDF
pdf_file = '../Angaza-Tumaini-Documentation.pdf'

class HeaderCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        page_count = len(self.pages)
        for page_num, page in enumerate(self.pages, 1):
            self.__dict__.update(page)
            self.draw_page_decoration(page_num, page_count)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_decoration(self, page_num, total_pages):
        self.setFillColor(HexColor('#1D4ED8'))
        self.rect(0, letter[1] - 0.5*inch, letter[0], 0.5*inch, fill=1, stroke=0)
        self.setFont('Helvetica', 8)
        self.setFillColor(HexColor('#6B7280'))
        self.drawString(0.75*inch, 0.3*inch, 'Angaza Tumaini Mission Center')
        self.drawRightString(letter[0] - 0.75*inch, 0.3*inch, f'Page {page_num} of {total_pages}')

doc = SimpleDocTemplate(pdf_file, pagesize=letter,
                        rightMargin=0.75*inch, leftMargin=0.75*inch,
                        topMargin=1*inch, bottomMargin=0.6*inch,
                        canvasmaker=HeaderCanvas)

# Color scheme
primary_color = HexColor('#1D4ED8')
secondary_color = HexColor('#10B981')
accent_color = HexColor('#FBBF24')
dark_color = HexColor('#1F2937')
light_gray = HexColor('#F3F4F6')

# Enhanced Styles
styles = getSampleStyleSheet()

title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=28, textColor=primary_color, spaceAfter=6, alignment=TA_CENTER, fontName='Helvetica-Bold')
subtitle_style = ParagraphStyle('Subtitle', parent=styles['Normal'], fontSize=11, textColor=HexColor('#6B7280'), spaceAfter=18, alignment=TA_CENTER, fontName='Helvetica')
body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=10, spaceAfter=8, textColor=dark_color, alignment=TA_JUSTIFY, fontName='Helvetica')
bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'], fontSize=10, spaceAfter=6, textColor=dark_color, leftIndent=20, fontName='Helvetica')

# Content
story = []

story.append(Spacer(1, 0.1*inch))
story.append(Paragraph('Angaza Tumaini Mission Center', title_style))
story.append(Paragraph('Project Documentation & Professional Invoice', subtitle_style))
story.append(Spacer(1, 0.1*inch))

# Overview
overview_data = [['📋 <b>Project Overview</b><br/><br/>A modern, responsive website built with HTML5, Tailwind CSS, and JavaScript. Multiple pages including Home, Contact, and Newsletter sections with local assets and optimized PNG icons.']]
overview_table = Table(overview_data, colWidths=[7.5*inch])
overview_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), light_gray), ('LEFTPADDING', (0, 0), (-1, -1), 15), ('RIGHTPADDING', (0, 0), (-1, -1), 15), ('TOPPADDING', (0, 0), (-1, -1), 12), ('BOTTOMPADDING', (0, 0), (-1, -1), 12), ('BORDER', (0, 0), (-1, -1), 1), ('BORDERCOLOR', (0, 0), (-1, -1), HexColor('#E5E7EB'))]))
story.append(overview_table)
story.append(Spacer(1, 0.2*inch))

# Timeline
timeline_data = [['🚀 Development Timeline']]
timeline_table = Table(timeline_data, colWidths=[7.5*inch])
timeline_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), primary_color), ('TEXTCOLOR', (0, 0), (-1, -1), white), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), 12), ('LEFTPADDING', (0, 0), (-1, -1), 15), ('TOPPADDING', (0, 0), (-1, -1), 10), ('BOTTOMPADDING', (0, 0), (-1, -1), 10)]))
story.append(timeline_table)
story.append(Spacer(1, 0.1*inch))

phases = [
    ('Phase 1: Scaffolding', 'Static HTML with Tailwind CSS and Lucide icons.'),
    ('Phase 2: Icon Refinement', 'SVG to PNG conversion for cross-platform consistency.'),
    ('Phase 3: Newsletter Integration', 'Created dedicated newsletter.html page.'),
    ('Phase 4: Contact Details', 'Clickable mailto, tel, WhatsApp links integrated.'),
    ('Phase 5: Mail Fallback', 'Intelligent Gmail compose fallback for email client compatibility.'),
    ('Phase 6: UI Polish', 'Circular PNG icons and restored header navigation.'),
    ('Phase 7: Deployment', 'Deployed to Vercel with GitHub integration.'),
]

for phase, desc in phases:
    story.append(Paragraph(f'<b>{phase}</b> — {desc}', bullet_style))

story.append(Spacer(1, 0.15*inch))

# Files Changed
files_data = [['📁 Key Files Modified']]
files_table = Table(files_data, colWidths=[7.5*inch])
files_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), primary_color), ('TEXTCOLOR', (0, 0), (-1, -1), white), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), 12), ('LEFTPADDING', (0, 0), (-1, -1), 15), ('TOPPADDING', (0, 0), (-1, -1), 10), ('BOTTOMPADDING', (0, 0), (-1, -1), 10)]))
story.append(files_table)
story.append(Spacer(1, 0.1*inch))

files = [
    ('<b>index.html</b>', 'Footer icons, mailto/tel links, mail fallback script, WhatsApp integration.'),
    ('<b>contact.html</b>', 'Clickable contact info, Formspree form with email fallback.'),
    ('<b>newsletter.html</b>', 'Social links and email subscription page.'),
    ('<b>filez/icons/</b>', 'PNG assets (Facebook, Instagram, Gmail, TikTok, WhatsApp).'),
]

for fname, desc in files:
    story.append(Paragraph(f'{fname} — {desc}', bullet_style))

story.append(Spacer(1, 0.15*inch))

# Preview & Deployment
preview_data = [['💻 How to Preview']]
preview_table = Table(preview_data, colWidths=[7.5*inch])
preview_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), secondary_color), ('TEXTCOLOR', (0, 0), (-1, -1), white), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), 12), ('LEFTPADDING', (0, 0), (-1, -1), 15), ('TOPPADDING', (0, 0), (-1, -1), 10), ('BOTTOMPADDING', (0, 0), (-1, -1), 10)]))
story.append(preview_table)
story.append(Spacer(1, 0.08*inch))
story.append(Paragraph('<font face="Courier">python -m http.server 8000</font>', body_style))
story.append(Paragraph('Then open <b>http://127.0.0.1:8000/index.html</b>', body_style))
story.append(Spacer(1, 0.15*inch))

deploy_data = [['🚀 Deployment']]
deploy_table = Table(deploy_data, colWidths=[7.5*inch])
deploy_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), secondary_color), ('TEXTCOLOR', (0, 0), (-1, -1), white), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), 12), ('LEFTPADDING', (0, 0), (-1, -1), 15), ('TOPPADDING', (0, 0), (-1, -1), 10), ('BOTTOMPADDING', (0, 0), (-1, -1), 10)]))
story.append(deploy_table)
story.append(Spacer(1, 0.08*inch))
story.append(Paragraph('<b>Vercel:</b> Live at <font face="Courier">npx vercel --prod</font>', body_style))
story.append(Paragraph('<b>GitHub:</b> <font face="Courier">https://github.com/alvingavi0/Angaza-Tumaini</font>', body_style))
story.append(Spacer(1, 0.15*inch))

# Screenshots
screenshots_data = [['📸 Screenshots']]
screenshots_table = Table(screenshots_data, colWidths=[7.5*inch])
screenshots_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), HexColor('#F97316')), ('TEXTCOLOR', (0, 0), (-1, -1), white), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), 12), ('LEFTPADDING', (0, 0), (-1, -1), 15), ('TOPPADDING', (0, 0), (-1, -1), 10), ('BOTTOMPADDING', (0, 0), (-1, -1), 10)]))
story.append(screenshots_table)
story.append(Spacer(1, 0.08*inch))
for i, s in enumerate(['Home Page (index.html)', 'Contact Page (contact.html)', 'Newsletter Page (newsletter.html)'], 1):
    story.append(Paragraph(f'<b>Screenshot {i}:</b> {s}', bullet_style))
    story.append(Spacer(1, 0.2*inch))

story.append(PageBreak())

# INVOICE SECTION
invoice_header = [['💳 PROFESSIONAL INVOICE']]
invoice_header_table = Table(invoice_header, colWidths=[7.5*inch])
invoice_header_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), accent_color), ('TEXTCOLOR', (0, 0), (-1, -1), dark_color), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), 14), ('LEFTPADDING', (0, 0), (-1, -1), 15), ('TOPPADDING', (0, 0), (-1, -1), 12), ('BOTTOMPADDING', (0, 0), (-1, -1), 12)]))
story.append(invoice_header_table)
story.append(Spacer(1, 0.2*inch))

# Details table
details = [['Invoice Date:', datetime.now().strftime('%B %d, %Y')], ['Client:', 'Angaza Tumaini Mission Center'], ['Service:', 'Web Development & Deployment']]
details_table = Table(details, colWidths=[2.5*inch, 5*inch])
details_table.setStyle(TableStyle([('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), 10), ('LEFTPADDING', (0, 0), (-1, -1), 12), ('TOPPADDING', (0, 0), (-1, -1), 10), ('BOTTOMPADDING', (0, 0), (-1, -1), 10), ('BOX', (0, 0), (-1, -1), 1, HexColor('#E5E7EB')), ('LINEBELOW', (0, -1), (-1, -1), 1, HexColor('#E5E7EB'))]))
story.append(details_table)
story.append(Spacer(1, 0.3*inch))

# Service breakdown
services = [['SERVICE DESCRIPTION', 'AMOUNT'], ['Web Development (HTML, CSS, JavaScript)', 'KES 15,000'], ['Deployment & Git Integration (Vercel)', 'KES 4,000'], ['Documentation & Support', 'KES 2,000'], ['', ''], ['TOTAL DUE', 'KES 21,000']]
services_table = Table(services, colWidths=[5.5*inch, 2*inch])
services_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), primary_color), ('TEXTCOLOR', (0, 0), (-1, 0), white), ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, 0), 11), ('BACKGROUND', (0, -1), (-1, -1), accent_color), ('TEXTCOLOR', (0, -1), (-1, -1), dark_color), ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, -1), (-1, -1), 12), ('ALIGN', (1, 1), (1, -1), 'RIGHT'), ('LEFTPADDING', (0, 0), (-1, -1), 12), ('TOPPADDING', (0, 0), (-1, -1), 12), ('BOTTOMPADDING', (0, 0), (-1, -1), 12), ('BOX', (0, 0), (-1, -1), 1, HexColor('#E5E7EB')), ('LINEBELOW', (0, 0), (-1, 0), 1, HexColor('#E5E7EB')), ('LINEBELOW', (0, -1), (-1, -1), 1, HexColor('#E5E7EB'))]))
story.append(services_table)
story.append(Spacer(1, 0.25*inch))

# Payment info
payment_data = [['💰 PAYMENT DETAILS']]
payment_table = Table(payment_data, colWidths=[7.5*inch])
payment_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), light_gray), ('TEXTCOLOR', (0, 0), (-1, -1), primary_color), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), 11), ('LEFTPADDING', (0, 0), (-1, -1), 15), ('TOPPADDING', (0, 0), (-1, -1), 10), ('BOTTOMPADDING', (0, 0), (-1, -1), 10), ('BORDER', (0, 0), (-1, -1), 1), ('BORDERCOLOR', (0, 0), (-1, -1), primary_color)]))
story.append(payment_table)
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph('<b>Method:</b> Mobile Money / Phone Transfer', body_style))
story.append(Paragraph('<b>Phone:</b> <font face="Courier"><b>0759106034</b></font>', body_style))
story.append(Paragraph('<b>Currency:</b> Kenyan Shillings (KES)', body_style))
story.append(Paragraph('<b>Reference:</b> Angaza-Tumaini-2025-Nov', body_style))
story.append(Spacer(1, 0.2*inch))

# Terms
terms_data = [['📋 TERMS & CONDITIONS']]
terms_table = Table(terms_data, colWidths=[7.5*inch])
terms_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), light_gray), ('TEXTCOLOR', (0, 0), (-1, -1), dark_color), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), 10), ('LEFTPADDING', (0, 0), (-1, -1), 15), ('TOPPADDING', (0, 0), (-1, -1), 10), ('BOTTOMPADDING', (0, 0), (-1, -1), 10), ('BORDER', (0, 0), (-1, -1), 1), ('BORDERCOLOR', (0, 0), (-1, -1), HexColor('#E5E7EB'))]))
story.append(terms_table)
story.append(Spacer(1, 0.1*inch))
terms = ['Website live on Vercel with Git integration and auto-deployment.', 'Full source code on GitHub repository.', 'Support & minor updates available for 30 days post-launch.', 'All code and assets property of Angaza Tumaini Mission Center.', 'Optional: Newsletter provider integration available.']
for term in terms:
    story.append(Paragraph(f'✓ {term}', bullet_style))

story.append(Spacer(1, 0.2*inch))
story.append(Paragraph('Thank you for partnering with us. For support, use the website contact form.', body_style))
story.append(Spacer(1, 0.05*inch))
story.append(Paragraph(f'Generated: {datetime.now().strftime("%B %d, %Y at %H:%M:%S")}', ParagraphStyle('Footer', parent=styles['Normal'], fontSize=8, textColor=HexColor('#9CA3AF'), alignment=TA_CENTER)))

doc.build(story)
print('✓ Professional PDF created: Angaza-Tumaini-Documentation.pdf')
