#!/usr/bin/env python3
"""
Angaza Tumaini Mission Center - Complete Comprehensive Guide
Single Document: User Manual + Documentation + FAQ + Billing
Generated: November 29, 2025
Style: Professional Modern & Classic with unified design
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.platypus import KeepTogether
from datetime import datetime

# Color Scheme (Modern & Classic)
PRIMARY_COLOR = HexColor('#1D4ED8')        # Deep Blue
SECONDARY_COLOR = HexColor('#10B981')      # Vibrant Green
ACCENT_COLOR = HexColor('#FBBF24')         # Gold
DARK_COLOR = HexColor('#1F2937')           # Charcoal
LIGHT_GRAY = HexColor('#F3F4F6')           # Light Gray
TEXT_COLOR = HexColor('#374151')           # Medium Gray

class HeaderFooterCanvas(canvas.Canvas):
    """Custom canvas with professional header and footer"""
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.page_num = 0
        
    def showPage(self):
        self.page_num += 1
        self._drawHeader()
        self._drawFooter()
        canvas.Canvas.showPage(self)
        
    def _drawHeader(self):
        """Draw professional header"""
        self.saveState()
        # Header bar
        self.setFillColor(PRIMARY_COLOR)
        self.rect(0, letter[1] - 0.5*inch, letter[0], 0.5*inch, fill=1, stroke=0)
        
        # Header text
        self.setFont("Helvetica-Bold", 10)
        self.setFillColor(white)
        self.drawString(0.5*inch, letter[1] - 0.25*inch, "Angaza Tumaini Mission Center — Complete Guide")
        self.drawRightString(letter[0] - 0.5*inch, letter[1] - 0.25*inch, f"Page {self.page_num}")
        self.restoreState()
        
    def _drawFooter(self):
        """Draw professional footer"""
        self.saveState()
        # Footer line
        self.setStrokeColor(LIGHT_GRAY)
        self.setLineWidth(1)
        self.line(0.5*inch, 0.4*inch, letter[0] - 0.5*inch, 0.4*inch)
        
        # Footer text
        self.setFont("Helvetica", 8)
        self.setFillColor(TEXT_COLOR)
        self.drawString(0.5*inch, 0.2*inch, "© 2025 Angaza Tumaini Mission Center | Kibera, Nairobi, Kenya")
        self.drawRightString(letter[0] - 0.5*inch, 0.2*inch, f"Generated: {datetime.now().strftime('%B %d, %Y')}")
        self.restoreState()

def create_comprehensive_guide():
    """Generate single comprehensive document"""
    filename = "Angaza-Tumaini-Comprehensive-Guide.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch,
        canvasmaker=HeaderFooterCanvas
    )
    
    styles = getSampleStyleSheet()
    
    # Title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=PRIMARY_COLOR,
        spaceAfter=12,
        alignment=1,
        fontName='Helvetica-Bold',
        letterSpacing=1
    )
    
    # Main heading
    main_heading = ParagraphStyle(
        'MainHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=white,
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold',
        backColor=PRIMARY_COLOR,
        borderPadding=12,
        alignment=0
    )
    
    # Section heading
    heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=PRIMARY_COLOR,
        spaceAfter=10,
        spaceBefore=10,
        fontName='Helvetica-Bold',
        borderColor=ACCENT_COLOR,
        borderWidth=2,
        borderPadding=8,
        backColor=LIGHT_GRAY
    )
    
    # Subsection
    subheading_style = ParagraphStyle(
        'SubHeading',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=SECONDARY_COLOR,
        spaceAfter=8,
        spaceBefore=8,
        fontName='Helvetica-Bold'
    )
    
    # Body text
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=10,
        textColor=TEXT_COLOR,
        alignment=4,
        spaceAfter=8,
        leading=14,
        fontName='Helvetica'
    )
    
    # Light body
    light_body = ParagraphStyle(
        'LightBody',
        parent=body_style,
        fontSize=9,
        textColor=HexColor('#6B7280'),
        alignment=0
    )
    
    story = []
    
    # ===== COVER PAGE =====
    story.append(Spacer(1, 1.5*inch))
    story.append(Paragraph("Angaza Tumaini", title_style))
    story.append(Paragraph("Mission Center", title_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Complete Comprehensive Guide", ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=16,
        textColor=SECONDARY_COLOR,
        alignment=1,
        spaceAfter=30,
        fontName='Helvetica-Bold'
    )))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Shining the Hope of Christ", ParagraphStyle(
        'Tagline',
        parent=styles['Normal'],
        fontSize=12,
        textColor=TEXT_COLOR,
        alignment=1,
        spaceAfter=12,
        fontName='Helvetica-Oblique'
    )))
    story.append(Spacer(1, 0.6*inch))
    
    # Document info
    doc_info = f"""
    <b>Website Launch:</b> October 11, 2025<br/>
    <b>Document Type:</b> Complete Organizational Guide<br/>
    <b>Generated:</b> {datetime.now().strftime('%B %d, %Y')}<br/><br/>
    <b>Location:</b> Olympic Estate, Kibera, Nairobi, Kenya<br/>
    <b>Email:</b> AngazaTumaini.org@gmail.com<br/>
    <b>Phone:</b> +254 716 475764<br/>
    <b>WhatsApp:</b> https://wa.link/xjt1s4
    """
    story.append(Paragraph(doc_info, light_body))
    
    story.append(PageBreak())
    
    # ===== TABLE OF CONTENTS =====
    story.append(Paragraph("📑 Table of Contents", heading_style))
    story.append(Spacer(1, 0.15*inch))
    
    toc_items = [
        "1. About Our Organization",
        "2. Our Founders & Leadership Team",
        "3. Mission, Vision & Values",
        "4. Our Five Core Programs",
        "5. How to Support Us",
        "6. Website Pages & Navigation",
        "7. Contact Information",
        "8. Frequently Asked Questions",
        "9. Project Details & Billing",
        "10. Technical Information"
    ]
    
    for item in toc_items:
        story.append(Paragraph(f"• {item}", body_style))
        story.append(Spacer(1, 0.08*inch))
    
    story.append(PageBreak())
    
    # ===== 1. ABOUT ORGANIZATION =====
    story.append(Paragraph("1. About Our Organization", main_heading))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("<b>🏠 Who We Are</b>", subheading_style))
    about_text = """
    Angaza Tumaini Mission Center is a Christian community-based ministry located in the heart of Kibera slums, Nairobi, Kenya. 
    Founded on the belief that every child has God-given potential and deserves hope, dignity, and opportunity, we are committed to 
    manifesting the hope of Christ in tangible, practical ways. Our center serves as a beacon of light in one of the most underserved areas of Nairobi, 
    providing safe spaces, spiritual guidance, educational support, and practical care to children, youth, and families.
    """
    story.append(Paragraph(about_text, body_style))
    
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph("<b>💡 Our Tagline</b>", subheading_style))
    story.append(Paragraph(
        "Angaza Tumaini is committed to manifesting the hope of Christ in tangible, practical ways, restoring dignity and purpose to those we serve.",
        ParagraphStyle('quote', parent=body_style, fontSize=10, italic=True, leftIndent=20, textColor=SECONDARY_COLOR)
    ))
    
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph("<b>📍 Location & Contact</b>", subheading_style))
    
    location_data = [
        ['Information', 'Details'],
        ['Address', 'Olympic Estate, Kibera, Nairobi, Kenya'],
        ['Email', 'AngazaTumaini.org@gmail.com'],
        ['Phone', '+254 716 475764'],
        ['WhatsApp', 'https://wa.link/xjt1s4'],
        ['Website', 'https://angaza-tumaini-o4nwg3zz9-calvin-wanyamas-projects.vercel.app'],
        ['Founded', 'October 11, 2025']
    ]
    
    loc_table = Table(location_data, colWidths=[2*inch, 3.5*inch])
    loc_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY_COLOR),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), LIGHT_GRAY),
        ('GRID', (0, 0), (-1, -1), 1, HexColor('#D1D5DB')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))
    story.append(loc_table)
    
    story.append(PageBreak())
    
    # ===== 2. LEADERSHIP TEAM =====
    story.append(Paragraph("2. Our Founders & Leadership Team", main_heading))
    story.append(Spacer(1, 0.15*inch))
    
    team_members = [
        ("Erick & Krista Baraza", "Founders & Missionaries", 
         """Erick and Krista Baraza are passionate missionaries who founded Angaza Tumaini. Married for over five years, they share a deep love for God 
         and a calling to bring hope to their community through Jesus Christ. Having been born and raised in Kibera, Erick understands the daily challenges 
         children and families face. This birthed a vision to create a place where children find safety, joy, hope, and encounter Christ's love.
         <br/><br/>Together, they are committed to raising a new generation grounded in God's word, equipped with education, and filled with hope for the future.
         <br/><br/><i>"Let your light shine before others, that they may see your good deeds and glorify your Father in heaven." – Matthew 5:16</i>"""),
        
        ("Evans Wandera", "Programs Coordinator",
         """Evans serves as Programs Coordinator, overseeing daily programs and ensuring every child receives care, mentorship, academic support, 
         and encounters Christ's love. Born and raised in Nairobi with a strong background in education and ministry, Evans brings practical experience 
         and a heart for discipleship. He creates programs that nurture faith, build character, and inspire hope, believing deeply that every child 
         has God-given potential.
         <br/><br/><i>"Train up a child in the way he should go, and when he is old, he will not depart from it." – Proverbs 22:6</i>"""),
        
        ("Jackline Mueni (Jay)", "Administrator & Programs Manager",
         """Jackline plays a key role in ensuring smooth operations and program delivery. With a heart for service and passion for empowering children 
         and families, Jackline combines organizational skills with deep love for God to create an environment where children thrive spiritually, 
         academically, and emotionally.
         <br/><br/><i>"Commit to the Lord whatever you do, and He will establish your plans." – Proverbs 16:3</i>"""),
        
        ("Felix Mito (Teacher Feloh)", "Tutor & Teacher",
         """Felix is a dedicated tutor guiding children in academic and faith matters. With a heart for teaching, Felix combines patience, creativity, 
         and Christ-centered approach to help children build strong academic foundations while encouraging spiritual and moral growth.
         <br/><br/><i>"Let the wise hear and increase in learning, and the one who understands obtain guidance." – Proverbs 1:5</i>"""),
        
        ("Naureen Mugeni (Chief Chef)", "Cook",
         """Naureen ensures every child receives nutritious and wholesome meals supporting their growth and well-being. With a heart for service and care, 
         she provides not only physical nourishment but also a sense of love and warmth.
         <br/><br/><i>"So, whether you eat or drink or whatever you do, do it all for the glory of God." – 1 Corinthians 10:31</i>"""),
        
        ("Benard Owira (Benah)", "Support Staff",
         """Benard serves faithfully as support staff, ensuring the center runs smoothly and remains clean, safe, and welcoming. He reflects servant-leadership, 
         serving out of love for God and others.
         <br/><br/><i>"Whatever you do, work at it with all your heart, as working for the Lord, not for human masters." – Colossians 3:23</i>""")
    ]
    
    for name, role, bio in team_members:
        story.append(Paragraph(f"<b>{name}</b>", subheading_style))
        story.append(Paragraph(f"<i>{role}</i>", light_body))
        story.append(Paragraph(bio, body_style))
        story.append(Spacer(1, 0.12*inch))
    
    story.append(PageBreak())
    
    # ===== 3. MISSION, VISION, VALUES =====
    story.append(Paragraph("3. Mission, Vision & Core Values", main_heading))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("<b>🎯 Our Mission</b>", subheading_style))
    story.append(Paragraph(
        "To bring the light and love of Jesus Christ to children and families of Kibera by providing a safe space for learning, nourishment, "
        "discipleship, and spiritual growth, manifesting the hope of Christ in tangible, practical ways.",
        ParagraphStyle('quote', parent=body_style, fontSize=10, italic=True, leftIndent=20, textColor=PRIMARY_COLOR)
    ))
    
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph("<b>🌟 Our Vision</b>", subheading_style))
    story.append(Paragraph(
        "Raising a new generation grounded in God's word, equipped with quality education, and filled with hope for the future. A community "
        "where every child knows their worth in Christ and has tools to build purposeful, productive lives.",
        ParagraphStyle('quote', parent=body_style, fontSize=10, italic=True, leftIndent=20, textColor=SECONDARY_COLOR)
    ))
    
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph("<b>💎 Our Core Values</b>", subheading_style))
    
    values = [
        ("✝️ Faith-Centered", "Gospel of Jesus Christ is at the heart of all we do"),
        ("💚 Community Empowerment", "Empowering individuals for self-sufficiency and hope"),
        ("📚 Education Excellence", "Quality education transforming lives and futures"),
        ("🤝 Dignity & Respect", "Recognizing inherent worth of every person"),
        ("🌟 Hope & Purpose", "Restoring hope and discovering God-given potential"),
        ("💪 Servant Leadership", "Leading by example with love and commitment")
    ]
    
    for title, desc in values:
        story.append(Paragraph(f"<b>{title}:</b> {desc}", body_style))
        story.append(Spacer(1, 0.06*inch))
    
    story.append(PageBreak())
    
    # ===== 4. PROGRAMS =====
    story.append(Paragraph("4. Our Five Core Programs", main_heading))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph(
        "We deliver holistic support through five comprehensive programs addressing spiritual, educational, social, and economic needs.",
        body_style
    ))
    story.append(Spacer(1, 0.12*inch))
    
    programs = [
        ("1. FAITH Program", "Spiritual Formation & Discipleship",
         "Bible study, Scripture memorization, discipleship mentorship, prayer and worship, character development, youth fellowship, and community service.",
         "Children develop strong Christian foundation, learn biblical principles, and become future leaders grounded in Christ-centered values."),
        
        ("2. Education Program", "Academic Excellence & Literacy",
         "After-school tutoring (Math, English, Science), literacy support, homework assistance, reading clubs, academic mentorship, and learning materials access.",
         "Children improve academic performance, develop confident learning habits, and are empowered to pursue higher education and opportunities."),
        
        ("3. Life-Skills Program", "Practical & Soft Skills",
         "Communication, public speaking, leadership, teamwork, decision-making, financial literacy, conflict resolution, health education, and career guidance.",
         "Youth develop confidence, resilience, and practical skills needed for informed decisions, healthy relationships, and career navigation."),
        
        ("4. Socio-Economic Empowerment", "Skills Training & Entrepreneurship",
         "Vocational skills (tailoring, hairdressing, welding, carpentry), entrepreneurship, microfinance, equipment support, market linkage, and job placement.",
         "Families achieve economic self-sufficiency, youth gain marketable skills, and community experiences reduced poverty through sustainable livelihoods."),
        
        ("5. Community Outreach", "Practical Ministry & Care",
         "Food distribution, medical clinics, health screening, clean water initiatives, school supplies, emergency relief, home visitation, and family support.",
         "Families experience Christ's love, immediate needs are met, health outcomes improve, and community experiences transformation through compassionate service.")
    ]
    
    for title, subtitle, activities, impact in programs:
        story.append(Paragraph(f"<b>{title}</b>", subheading_style))
        story.append(Paragraph(f"<i>{subtitle}</i>", light_body))
        story.append(Paragraph(f"<b>Activities:</b> {activities}", body_style))
        story.append(Paragraph(f"<b>Impact:</b> {impact}", body_style))
        story.append(Spacer(1, 0.12*inch))
    
    story.append(PageBreak())
    
    # ===== 5. HOW TO SUPPORT =====
    story.append(Paragraph("5. How to Support Our Mission", main_heading))
    story.append(Spacer(1, 0.15*inch))
    
    support_methods = [
        ("💰 Financial Donation", 
         "Support programs through contributions for meals, education, vocational training, medical services, and program materials. "
         "Use 'GIVE HOPE' button on website or contact for payment instructions."),
        
        ("🤝 Volunteer Your Time",
         "Education tutoring, faith/discipleship mentoring, healthcare education, skills training, organizational support, community outreach. "
         "Contact us to match your skills with volunteer opportunities."),
        
        ("🏢 Corporate Partnerships",
         "In-kind donations, corporate volunteering, program sponsorship, internship and job placement opportunities. Contact for partnership options."),
        
        ("👦 Sponsor a Child",
         "Provide education support, daily meals, school supplies, health services, and spiritual mentorship. Make long-term impact on a child's life."),
        
        ("📧 Stay Connected",
         "Subscribe to newsletter, follow social media, share our story, pray for the mission, advocate for social justice and community development.")
    ]
    
    for title, desc in support_methods:
        story.append(Paragraph(f"<b>{title}</b>", subheading_style))
        story.append(Paragraph(desc, body_style))
        story.append(Spacer(1, 0.1*inch))
    
    story.append(PageBreak())
    
    # ===== 6. WEBSITE PAGES =====
    story.append(Paragraph("6. Website Pages & Navigation", main_heading))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("<b>🏠 Home Page (index.html)</b>", subheading_style))
    home_desc = """
    <b>Sections:</b> Hero with rotating images, About Us with team profiles, Our Programs (5 cards), Our Impact (animated counters), 
    Get Involved (ways to support), Contact form, Footer with socials.<br/>
    <b>Key Actions:</b> Learn about organization, view team, explore programs, see impact, contact, donate via GIVE HOPE button.
    """
    story.append(Paragraph(home_desc, body_style))
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("<b>📞 Contact Page (contact.html)</b>", subheading_style))
    contact_desc = """
    <b>Features:</b> Contact form (email backend), direct channels (email, phone, WhatsApp), address, social media links.<br/>
    <b>Best For:</b> General inquiries, partnership discussions, volunteer interest, donations, meeting the team.
    """
    story.append(Paragraph(contact_desc, body_style))
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("<b>📧 Newsletter Page (newsletter.html)</b>", subheading_style))
    news_desc = """
    <b>Features:</b> Newsletter signup, Follow Us section (social icons), share buttons, links to all social channels.<br/>
    <b>Best For:</b> Stay updated, follow on social media, share content with your network.
    """
    story.append(Paragraph(news_desc, body_style))
    
    story.append(PageBreak())
    
    # ===== 7. CONTACT =====
    story.append(Paragraph("7. Contact Information & Support", main_heading))
    story.append(Spacer(1, 0.15*inch))
    
    contact_methods = [
        ['Method', 'Details', 'Best For'],
        ['Email', 'AngazaTumaini.org@gmail.com', 'Detailed inquiries, applications, feedback'],
        ['Phone', '+254 716 475764', 'Urgent matters, immediate conversation'],
        ['WhatsApp', 'https://wa.link/xjt1s4', 'Quick messages, group inquiries, updates'],
        ['Facebook', 'https://www.facebook.com/profile.php?id=61552268876833', 'Updates, community engagement, sharing'],
        ['Website Form', 'Contact page on site', 'General inquiries, feedback'],
        ['In-Person', 'Olympic Estate, Kibera, Nairobi', 'Volunteer intake, center visits, meetings']
    ]
    
    contact_table = Table(contact_methods, colWidths=[1.3*inch, 2.2*inch, 1.8*inch])
    contact_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), SECONDARY_COLOR),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), white),
        ('GRID', (0, 0), (-1, -1), 1, HexColor('#D1D5DB')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    story.append(contact_table)
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Response Time:</b> We aim to respond within 24-48 hours. For urgent matters, please call or use WhatsApp.", light_body))
    
    story.append(PageBreak())
    
    # ===== 8. FAQ =====
    story.append(Paragraph("8. Frequently Asked Questions", main_heading))
    story.append(Spacer(1, 0.15*inch))
    
    faqs = [
        ("What is Angaza Tumaini?",
         "A Christian community-based ministry in Kibera serving children and families through five programs: Faith, Education, Life-Skills, "
         "Socio-economic Empowerment, and Community Outreach."),
        
        ("When was it founded?",
         "Founded by Erick and Krista Baraza. Website launched October 11, 2025."),
        
        ("Where is it located?",
         "Olympic Estate, Kibera, Nairobi, Kenya."),
        
        ("How can I support?",
         "Financial donation, volunteer, become corporate partner, sponsor a child, subscribe to newsletter, or share our story."),
        
        ("How do I volunteer?",
         "Contact AngazaTumaini.org@gmail.com, +254 716 475764, or WhatsApp https://wa.link/xjt1s4. We welcome volunteers in education, "
         "mentoring, healthcare, skilled trades, and general support."),
        
        ("Can I sponsor a child?",
         "Yes! Child sponsorship provides education, meals, and spiritual development. Contact us to discuss opportunities."),
        
        ("How is my donation used?",
         "Donations support our five core programs: spiritual formation, academic tutoring, life-skills, livelihood support, and community outreach."),
        
        ("Is there a newsletter?",
         "Yes! Visit the Newsletter page or click 'JOIN OUR NEWSLETTER' in footer to stay updated on programs, events, and impact stories."),
        
        ("What are operating hours?",
         "Contact us directly at AngazaTumaini.org@gmail.com or +254 716 475764 for specific hours and program schedules."),
        
        ("How do I provide feedback?",
         "Use the contact form, email us, or call directly. Your feedback helps us improve our services.")
    ]
    
    for i, (q, a) in enumerate(faqs, 1):
        story.append(Paragraph(f"<b>Q{i}: {q}</b>", subheading_style))
        story.append(Paragraph(f"<b>A:</b> {a}", body_style))
        story.append(Spacer(1, 0.08*inch))
    
    story.append(PageBreak())
    
    # ===== 9. PROJECT DETAILS & BILLING =====
    story.append(Paragraph("9. Project Details & Billing", main_heading))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("<b>💻 Website Project Overview</b>", subheading_style))
    story.append(Paragraph(
        "<b>Project Name:</b> Angaza Tumaini Mission Center Website<br/>"
        "<b>Launch Date:</b> October 11, 2025<br/>"
        "<b>Type:</b> Static responsive website with modern design<br/>"
        "<b>Status:</b> Live and fully functional<br/>"
        "<b>Live URL:</b> https://angaza-tumaini-o4nwg3zz9-calvin-wanyamas-projects.vercel.app",
        body_style
    ))
    
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph("<b>💳 Billing Information</b>", subheading_style))
    
    billing_data = [
        ['Service', 'Description', 'Amount'],
        ['Web Development', 'HTML5, CSS3, JavaScript, responsive design, color scheme', 'KES 15,000'],
        ['Deployment', 'Vercel hosting, Git integration, auto-deployment', 'KES 4,000'],
        ['Documentation', 'User manuals, guides, comprehensive documentation', 'KES 2,000'],
        ['TOTAL', 'Complete website with documentation', 'KES 21,000']
    ]
    
    bill_table = Table(billing_data, colWidths=[1.5*inch, 2.8*inch, 1.3*inch])
    bill_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY_COLOR),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (2, 0), (2, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, -1), (-1, -1), ACCENT_COLOR),
        ('TEXTCOLOR', (0, -1), (-1, -1), DARK_COLOR),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, HexColor('#D1D5DB')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -2), [white, LIGHT_GRAY]),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))
    story.append(bill_table)
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(
        "<b>Payment Method:</b> Mobile Money / Phone Transfer<br/>"
        "<b>Payment Number:</b> 0759106034<br/>"
        "<b>Reference:</b> Angaza-Tumaini-2025-Oct<br/>"
        "<b>Payment Terms:</b> Upon project completion",
        body_style
    ))
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>📋 Deliverables Completed</b>", subheading_style))
    
    deliverables = [
        "✅ Responsive website (desktop, tablet, mobile)",
        "✅ Three main pages: Home, Contact, Newsletter",
        "✅ Professional color scheme and modern design",
        "✅ Integrated contact form (Formspree backend)",
        "✅ Social media integration (5 platforms)",
        "✅ Live deployment on Vercel",
        "✅ GitHub repository with version control",
        "✅ Comprehensive documentation and user manuals",
        "✅ SEO optimization and accessibility features",
        "✅ Email fallback for mailto: links"
    ]
    
    for item in deliverables:
        story.append(Paragraph(item, body_style))
        story.append(Spacer(1, 0.06*inch))
    
    story.append(PageBreak())
    
    # ===== 10. TECHNICAL =====
    story.append(Paragraph("10. Technical Information", main_heading))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("<b>🛠️ Technology Stack</b>", subheading_style))
    
    tech_data = [
        ['Component', 'Technology', 'Purpose'],
        ['Frontend', 'HTML5, CSS3, JavaScript', 'User interface and interactions'],
        ['Styling', 'Tailwind CSS + Custom CSS', 'Responsive design and theming'],
        ['Icons', 'Lucide Icons + PNG Images', 'Visual elements and branding'],
        ['Fonts', 'Poppins, Inter', 'Professional typography'],
        ['Form Backend', 'Formspree', 'Email form submissions'],
        ['Hosting', 'Vercel', 'Fast, reliable static hosting'],
        ['Version Control', 'GitHub', 'Source code management'],
        ['Color Scheme', 'Blue #1D4ED8, Green #10B981, Gold #FBBF24', 'Brand colors']
    ]
    
    tech_table = Table(tech_data, colWidths=[1.4*inch, 1.8*inch, 2.3*inch])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY_COLOR),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), white),
        ('GRID', (0, 0), (-1, -1), 1, HexColor('#D1D5DB')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    story.append(tech_table)
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>♿ Accessibility Features</b>", subheading_style))
    
    a11y_features = [
        "✓ Responsive design (works on all devices)",
        "✓ Clear, intuitive navigation",
        "✓ Readable typography with good contrast",
        "✓ Alt text on all images",
        "✓ WCAG accessibility standards",
        "✓ Semantic HTML structure",
        "✓ Mobile-friendly touch targets",
        "✓ Keyboard navigation support"
    ]
    
    for feature in a11y_features:
        story.append(Paragraph(feature, body_style))
        story.append(Spacer(1, 0.06*inch))
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>🌐 Browser Compatibility</b>", subheading_style))
    story.append(Paragraph(
        "Chrome/Chromium (latest), Firefox (latest), Safari (latest), Edge (latest), Mobile browsers (iOS Safari, Chrome Mobile). "
        "For best experience, keep your browser updated.",
        body_style
    ))
    
    story.append(PageBreak())
    
    # ===== CLOSING =====
    story.append(Spacer(1, 1*inch))
    
    story.append(Paragraph("Thank You", title_style))
    story.append(Spacer(1, 0.3*inch))
    
    closing = """
    We are grateful for every person who takes time to learn about Angaza Tumaini's mission and considers how they might support our work. 
    Whether through prayer, volunteering, donation, or sharing our story, your involvement makes a real difference in the lives of children 
    and families in Kibera.<br/><br/>
    
    At Angaza Tumaini, we believe that every child has God-given potential and deserves hope, dignity, and opportunity. Together, 
    we are shining the light of Christ in one of the most underserved areas of Nairobi.<br/><br/>
    
    <b>Get Involved Today:</b><br/>
    📧 Email: AngazaTumaini.org@gmail.com<br/>
    📞 Phone: +254 716 475764<br/>
    💬 WhatsApp: https://wa.link/xjt1s4<br/>
    🌐 Website: https://angaza-tumaini-o4nwg3zz9-calvin-wanyamas-projects.vercel.app<br/><br/>
    
    <i>"Let your light shine before others, that they may see your good deeds and glorify your Father in heaven." – Matthew 5:16</i>
    """
    story.append(Paragraph(closing, body_style))
    
    story.append(Spacer(1, 0.4*inch))
    
    story.append(Paragraph(
        "© 2025 Angaza Tumaini Mission Center. All rights reserved. Powered by faith, love, and the hope of Christ.",
        ParagraphStyle(
            'Footer',
            parent=styles['Normal'],
            fontSize=8,
            textColor=TEXT_COLOR,
            alignment=1,
            fontName='Helvetica-Oblique'
        )
    ))
    
    # Build PDF
    doc.build(story)
    print(f"✅ Complete Comprehensive Guide created: {filename}")
    print(f"   📄 Single document with all information")
    print(f"   📋 10 major sections covering everything")
    print(f"   🎨 Professional modern & classic theme throughout")
    print(f"   📏 Consistent styling and unified design")

if __name__ == "__main__":
    create_comprehensive_guide()
