#!/usr/bin/env python3
"""
Angaza Tumaini Mission Center - Comprehensive User Manual & Website Documentation
Generated: November 29, 2025
Purpose: Complete user guide for website navigation and organization mission details
Style: Modern & Classic with professional typography and color scheme
"""

from reportlab.lib.pagesizes import letter, A4
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

class HeaderCanvas(canvas.Canvas):
    """Custom canvas with header and footer for professional look"""
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
        self.drawString(0.5*inch, letter[1] - 0.25*inch, "Angaza Tumaini Mission Center — Website User Manual")
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
        self.drawString(0.5*inch, 0.2*inch, "© 2025 Angaza Tumaini Mission Center | Located in Kibera, Nairobi, Kenya")
        self.drawRightString(letter[0] - 0.5*inch, 0.2*inch, f"Generated: {datetime.now().strftime('%B %d, %Y')}")
        self.restoreState()

def create_manual():
    """Generate comprehensive user manual PDF"""
    filename = "Angaza-Tumaini-Website-User-Manual.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch,
        canvasmaker=HeaderCanvas
    )
    
    # Custom styles
    styles = getSampleStyleSheet()
    
    # Title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=PRIMARY_COLOR,
        spaceAfter=12,
        alignment=1,  # Center
        fontName='Helvetica-Bold',
        letterSpacing=1
    )
    
    # Section heading style
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=PRIMARY_COLOR,
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold',
        borderColor=ACCENT_COLOR,
        borderWidth=2,
        borderPadding=10,
        backColor=LIGHT_GRAY
    )
    
    # Subsection style
    subheading_style = ParagraphStyle(
        'SubHeading',
        parent=styles['Heading3'],
        fontSize=13,
        textColor=SECONDARY_COLOR,
        spaceAfter=10,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    )
    
    # Body text style
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        textColor=TEXT_COLOR,
        alignment=4,  # Justify
        spaceAfter=10,
        leading=16,
        fontName='Helvetica'
    )
    
    # Light body for descriptions
    light_body = ParagraphStyle(
        'LightBody',
        parent=body_style,
        fontSize=10,
        textColor=HexColor('#6B7280'),
        alignment=0  # Left
    )
    
    # Story style (italic)
    story_style = ParagraphStyle(
        'StoryStyle',
        parent=body_style,
        fontSize=10,
        textColor=DARK_COLOR,
        italic=True,
        leftIndent=20,
        rightIndent=20,
        spaceAfter=12
    )
    
    story = []
    
    # ===== COVER PAGE =====
    story.append(Spacer(1, 1.5*inch))
    story.append(Paragraph("Angaza Tumaini Mission Center", title_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Website User Manual & Complete Guide", ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=18,
        textColor=SECONDARY_COLOR,
        alignment=1,
        spaceAfter=30,
        fontName='Helvetica-Bold'
    )))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Shining the Hope of Christ", ParagraphStyle(
        'Tagline',
        parent=styles['Normal'],
        fontSize=14,
        textColor=TEXT_COLOR,
        alignment=1,
        spaceAfter=12,
        fontName='Helvetica-Oblique'
    )))
    story.append(Paragraph("Through Practical Programs: Faith Formation, Education, Life-Skills & Community Empowerment", 
                          light_body))
    
    story.append(Spacer(1, 0.8*inch))
    
    # Document info
    doc_info = f"""
    <b>Website Launch:</b> October 11, 2025<br/>
    <b>Document Generated:</b> {datetime.now().strftime('%B %d, %Y')}<br/>
    <b>Location:</b> Olympic Estate, Kibera, Nairobi, Kenya<br/>
    <b>Primary Contact:</b> AngazaTumaini.org@gmail.com<br/>
    <b>Phone:</b> +254 716 475764<br/>
    <b>WhatsApp:</b> https://wa.link/xjt1s4
    """
    story.append(Paragraph(doc_info, light_body))
    
    story.append(PageBreak())
    
    # ===== TABLE OF CONTENTS =====
    story.append(Paragraph("Table of Contents", heading_style))
    story.append(Spacer(1, 0.2*inch))
    
    toc_items = [
        "1. About Angaza Tumaini Mission Center",
        "2. Our Founders & Leadership Team",
        "3. Our Mission, Vision & Values",
        "4. Our Five Core Programs",
        "5. Website Overview & Navigation",
        "6. How to Use Each Page",
        "7. Contact & Support",
        "8. Frequently Asked Questions (FAQ)",
        "9. Getting Involved - Ways to Support",
        "10. Technical Details & Accessibility"
    ]
    
    for item in toc_items:
        story.append(Paragraph(f"• {item}", body_style))
        story.append(Spacer(1, 0.1*inch))
    
    story.append(PageBreak())
    
    # ===== 1. ABOUT SECTION =====
    story.append(Paragraph("1. About Angaza Tumaini Mission Center", heading_style))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph(
        "<b>Who We Are</b>",
        subheading_style
    ))
    
    about_text = """
    Angaza Tumaini Mission Center is a community-based Christian ministry located in the heart of Kibera slums, Nairobi, Kenya. 
    Founded on the belief that every child has God-given potential and deserves hope, dignity, and opportunity, we are committed to 
    manifesting the hope of Christ in tangible, practical ways.
    <br/><br/>
    Our center serves as a beacon of light in one of the most underserved areas of Nairobi, providing safe spaces, spiritual guidance, 
    educational support, and practical care to children, youth, and families navigating life's challenges.
    """
    story.append(Paragraph(about_text, body_style))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("<b>Our Tagline</b>", subheading_style))
    story.append(Paragraph(
        "Angaza Tumaini is committed to manifesting the hope of Christ in tangible, practical ways, restoring dignity and purpose to those we serve.",
        story_style
    ))
    
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph("<b>Location & Contact Information</b>", subheading_style))
    
    location_data = [
        ['Item', 'Details'],
        ['Address', 'Olympic Estate, Kibera, Nairobi, Kenya'],
        ['Email', 'AngazaTumaini.org@gmail.com'],
        ['Phone', '+254 716 475764'],
        ['WhatsApp', 'https://wa.link/xjt1s4'],
        ['Website', 'https://angaza-tumaini-o4nwg3zz9-calvin-wanyamas-projects.vercel.app'],
        ['Live Since', 'October 11, 2025']
    ]
    
    location_table = Table(location_data, colWidths=[2*inch, 3.5*inch])
    location_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY_COLOR),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), LIGHT_GRAY),
        ('GRID', (0, 0), (-1, -1), 1, HexColor('#D1D5DB')),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ]))
    story.append(location_table)
    
    story.append(PageBreak())
    
    # ===== 2. FOUNDERS & TEAM =====
    story.append(Paragraph("2. Our Founders & Leadership Team", heading_style))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("<b>Erick and Krista Baraza — Founders & Missionaries</b>", subheading_style))
    story.append(Paragraph(
        """Erick and Krista Baraza are passionate missionaries and the founders of Angaza Tumaini Mission Center. 
        Married for over five years, they share a deep love for God and a calling to bring hope and transformation to their community 
        through the Gospel of our Lord and Savior, Jesus Christ.<br/><br/>
        
        <b>Background:</b> Having been born and raised in Kibera, Erick understands the daily challenges children and families face. 
        This personal experience birthed a vision in his heart – to create a place where children can find safety, joy, and hope. 
        At Angaza Tumaini, kids have a space to play, study, receive a hot meal, and most importantly, encounter the love of Christ.<br/><br/>
        
        <b>Vision:</b> Together, Erick and Krista are committed to shining the light of Christ in one of the most underserved areas of Nairobi 
        – raising a new generation of young people grounded in God's word, equipped with education, and filled with hope for the future. 
        Their mission is to bring the light and love of Jesus Christ to the children and families of Kibera by providing a safe space 
        for learning, nourishment, discipleship, and spiritual growth.<br/><br/>
        
        <i>"Let your light shine before others, that they may see your good deeds and glorify your Father in heaven." – Matthew 5:16</i>
        """,
        body_style
    ))
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Evans Wandera — Programs Coordinator</b>", subheading_style))
    story.append(Paragraph(
        """Evans Wandera serves as the Programs Coordinator at Angaza Tumaini. Born and raised in Nairobi, Evans has always been 
        passionate about serving his community, especially children and youth living in challenging circumstances. With a strong background 
        in education and ministry, Evans brings both practical experience and a heart for discipleship to his role.<br/><br/>
        
        <b>Responsibilities:</b> Evans oversees the daily programs at Angaza Tumaini, ensuring that every child receives care, mentorship, 
        academic support, and most importantly, encounters the love of Christ. He believes deeply that every child has God-given potential. 
        Through his leadership, he creates programs that nurture faith, build character, and inspire hope.<br/><br/>
        
        <i>"Train up a child in the way he should go, and when he is old, he will not depart from it." – Proverbs 22:6</i>
        """,
        body_style
    ))
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Jackline Mueni (Jay) — Administrator & Programs Manager</b>", subheading_style))
    story.append(Paragraph(
        """Jackline Mueni serves as the Administrator and Programs Manager, playing a key role in ensuring the smooth running of 
        the mission's programs and operations. With a heart for service and a passion for empowering children and families, Jackline 
        combines organizational skills with a deep love for God to create an environment where children can thrive spiritually, academically, 
        and emotionally.<br/><br/>
        
        <i>"Commit to the Lord whatever you do, and He will establish your plans." – Proverbs 16:3</i>
        """,
        body_style
    ))
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Felix Mito (Teacher Feloh) — Tutor & Teacher</b>", subheading_style))
    story.append(Paragraph(
        """Felix serves as a dedicated tutor with a heart for teaching and guiding children in both academic and faith matters. 
        Born and raised in Nairobi, Felix has always believed in the transformative power of education. He combines patience, creativity, 
        and a Christ-centered approach to help children build strong academic foundations while encouraging spiritual and moral growth.<br/><br/>
        
        <i>"Let the wise hear and increase in learning, and the one who understands obtain guidance." – Proverbs 1:5</i>
        """,
        body_style
    ))
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Naureen Mugeni (Chief Chef) — Cook</b>", subheading_style))
    story.append(Paragraph(
        """Naureen Mugeni serves as the Cook, ensuring that every child at the center receives nutritious and wholesome meals supporting 
        their growth, health, and overall well-being. With a heart for service and care, Naureen provides not only physical nourishment 
        but also a sense of love and warmth through her work.<br/><br/>
        
        <i>"So, whether you eat or drink or whatever you do, do it all for the glory of God." – 1 Corinthians 10:31</i>
        """,
        body_style
    ))
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Benard Owira (Benah) — Support Staff</b>", subheading_style))
    story.append(Paragraph(
        """Benard serves faithfully as part of the Support staff, ensuring the center runs smoothly and remains clean, safe, and welcoming. 
        Taking great pride in his work, Benard views it as a way to serve God and support the mission's vision of bringing light and hope 
        to the community, reflecting the heart of servant-leadership.<br/><br/>
        
        <i>"Whatever you do, work at it with all your heart, as working for the Lord, not for human masters." – Colossians 3:23</i>
        """,
        body_style
    ))
    
    story.append(PageBreak())
    
    # ===== 3. MISSION, VISION & VALUES =====
    story.append(Paragraph("3. Our Mission, Vision & Values", heading_style))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("<b>Our Mission</b>", subheading_style))
    story.append(Paragraph(
        "To bring the light and love of Jesus Christ to the children and families of Kibera by providing a safe space for learning, "
        "nourishment, discipleship, and spiritual growth, manifesting the hope of Christ in tangible, practical ways.",
        story_style
    ))
    
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph("<b>Our Vision</b>", subheading_style))
    story.append(Paragraph(
        "Raising a new generation of young people grounded in God's word, equipped with quality education, and filled with hope for the future. "
        "We envision a community where every child knows their worth in Christ and has the tools to build a purposeful, productive life.",
        story_style
    ))
    
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph("<b>Our Core Values</b>", subheading_style))
    
    values = [
        ("✝️ Faith-Centered", "Everything we do is rooted in the Gospel of Jesus Christ. Our programs are designed not only to meet physical needs but also to nurture spiritual growth and discipleship."),
        ("💚 Community Empowerment", "We believe in empowering individuals and families to take charge of their futures through education, skills training, and practical support."),
        ("📚 Education Excellence", "Quality education is transformative. We provide academic support, mentorship, and life-skills training to equip children for success."),
        ("🤝 Dignity & Respect", "Every person deserves dignity and respect. We serve with humility, recognizing the inherent worth of all individuals."),
        ("🌟 Hope & Purpose", "We are committed to restoring hope and helping each person discover their God-given purpose and potential."),
        ("💪 Servant Leadership", "We lead by example, serving with love and commitment, recognizing that true leadership is about lifting others up.")
    ]
    
    for title, desc in values:
        story.append(Paragraph(f"<b>{title}</b>", subheading_style))
        story.append(Paragraph(desc, body_style))
        story.append(Spacer(1, 0.1*inch))
    
    story.append(PageBreak())
    
    # ===== 4. OUR PROGRAMS =====
    story.append(Paragraph("4. Our Five Core Programs", heading_style))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph(
        "At Angaza Tumaini, we deliver holistic support through five comprehensive programs designed to address the spiritual, educational, "
        "social, and economic needs of children and families. Each program is carefully crafted to deliver lasting impact.",
        body_style
    ))
    
    story.append(Spacer(1, 0.2*inch))
    
    # Program 1
    story.append(Paragraph("<b>1. FAITH Program (Spiritual Formation & Discipleship)</b>", subheading_style))
    story.append(Paragraph(
        """<b>Purpose:</b> Rooted in Christ's love, this program helps children and youth grow spiritually and live out their beliefs with confidence through mentorship and discipleship.<br/><br/>
        
        <b>Key Activities:</b><br/>
        • Bible study and Scripture memorization<br/>
        • Discipleship mentorship with trained leaders<br/>
        • Prayer and worship sessions<br/>
        • Character development and moral guidance<br/>
        • Youth fellowship and community service<br/><br/>
        
        <b>Impact:</b> Children develop a strong foundation in Christian faith, learn biblical principles for living, and are mentored to become 
        future leaders grounded in Christ-centered values. This program ensures that spiritual growth goes hand-in-hand with practical life application.
        """,
        body_style
    ))
    
    story.append(Spacer(1, 0.15*inch))
    
    # Program 2
    story.append(Paragraph("<b>2. Education Program (Academic Excellence & Literacy)</b>", subheading_style))
    story.append(Paragraph(
        """<b>Purpose:</b> Equips children and youth with the tools to learn, grow, and succeed through after-school tutoring, literacy support, and mentorship.<br/><br/>
        
        <b>Key Activities:</b><br/>
        • After-school tutoring in core subjects (Math, English, Science)<br/>
        • Literacy and numeracy support for younger children<br/>
        • Homework assistance and exam preparation<br/>
        • Reading clubs and educational games<br/>
        • Academic mentorship and goal-setting<br/>
        • Access to learning materials and resources<br/><br/>
        
        <b>Impact:</b> Children improve academic performance, develop confident learning habits, and are empowered to pursue higher education 
        and professional opportunities. The program bridges educational gaps and removes barriers to learning.
        """,
        body_style
    ))
    
    story.append(Spacer(1, 0.15*inch))
    
    # Program 3
    story.append(Paragraph("<b>3. Life-Skills Program (Practical & Soft Skills Training)</b>", subheading_style))
    story.append(Paragraph(
        """<b>Purpose:</b> Empowers participants with essential skills such as communication, decision-making, leadership, and financial literacy to navigate life's challenges.<br/><br/>
        
        <b>Key Activities:</b><br/>
        • Communication and public speaking workshops<br/>
        • Leadership and teamwork training<br/>
        • Decision-making and problem-solving skills<br/>
        • Financial literacy and budgeting education<br/>
        • Conflict resolution and emotional intelligence<br/>
        • Health, hygiene, and wellness education<br/>
        • Career guidance and vocational exploration<br/><br/>
        
        <b>Impact:</b> Youth develop confidence, resilience, and practical skills needed to make informed decisions, build healthy relationships, 
        and navigate career choices. These skills are essential for personal development and social integration.
        """,
        body_style
    ))
    
    story.append(Spacer(1, 0.15*inch))
    
    # Program 4
    story.append(Paragraph("<b>4. Socio-Economic Empowerment (Skills Training & Entrepreneurship)</b>", subheading_style))
    story.append(Paragraph(
        """<b>Purpose:</b> Equips individuals and families for financial independence through vocational training, entrepreneurship support, and local initiatives.<br/><br/>
        
        <b>Key Activities:</b><br/>
        • Vocational skills training (tailoring, hairdressing, welding, carpentry)<br/>
        • Entrepreneurship and business development training<br/>
        • Microfinance and savings group formation<br/>
        • Tool and equipment support for small businesses<br/>
        • Market linkage and sales training<br/>
        • Family income generation projects<br/>
        • Job placement assistance<br/><br/>
        
        <b>Impact:</b> Families move towards economic self-sufficiency, youth gain marketable skills, and the community sees reduced poverty 
        and increased economic participation. This program breaks the cycle of poverty through sustainable livelihood creation.
        """,
        body_style
    ))
    
    story.append(Spacer(1, 0.15*inch))
    
    # Program 5
    story.append(Paragraph("<b>5. Community Outreach (Practical Ministry & Care)</b>", subheading_style))
    story.append(Paragraph(
        """<b>Purpose:</b> Extends Christ's love to families through practical service, food drives, health campaigns, medical camps, and direct acts of care.<br/><br/>
        
        <b>Key Activities:</b><br/>
        • Food distribution and nutritional support<br/>
        • Medical clinics and health screening camps<br/>
        • Clean water and sanitation initiatives<br/>
        • School supply and uniform distribution<br/>
        • Emergency relief and disaster support<br/>
        • Home visitation and family counseling<br/>
        • Community cleaning and beautification projects<br/>
        • Holiday celebrations and family fellowships<br/><br/>
        
        <b>Impact:</b> Families experience tangible expressions of Christ's love, immediate needs are met, health outcomes improve, and 
        the community experiences transformation through compassionate service and sustainable development initiatives.
        """,
        body_style
    ))
    
    story.append(PageBreak())
    
    # ===== 5. WEBSITE OVERVIEW =====
    story.append(Paragraph("5. Website Overview & Navigation", heading_style))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph(
        """The Angaza Tumaini website is a modern, responsive platform designed to provide visitors with comprehensive information about our mission, 
        programs, team, and how to get involved. Launched on October 11, 2025, the website features an intuitive navigation system and 
        professional design that reflects our commitment to excellence and hope.""",
        body_style
    ))
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<b>Website Features</b>", subheading_style))
    
    features = [
        "🏠 Responsive Design: Works perfectly on desktop, tablet, and mobile devices",
        "🎨 Modern Color Scheme: Uses professional colors (Deep Blue, Vibrant Green, Gold) for visual impact",
        "📱 Mobile-Friendly Navigation: Easy access to all sections on all devices",
        "🖼️ Dynamic Image Galleries: Professional photography showcasing our work and community",
        "⚡ Fast Loading: Optimized for quick page loads and smooth scrolling",
        "🔍 SEO Optimized: Discoverable through search engines",
        "♿ Accessibility: Built with web standards for inclusive access",
        "🔗 Social Media Integration: Easy access to our social channels",
    ]
    
    for feature in features:
        story.append(Paragraph(f"• {feature}", body_style))
        story.append(Spacer(1, 0.08*inch))
    
    story.append(PageBreak())
    
    # ===== 6. PAGE-BY-PAGE GUIDE =====
    story.append(Paragraph("6. How to Use Each Page", heading_style))
    story.append(Spacer(1, 0.15*inch))
    
    # Home Page
    story.append(Paragraph("<b>HOME PAGE (index.html)</b>", subheading_style))
    story.append(Paragraph(
        """<b>What You'll Find:</b> The main landing page that introduces Angaza Tumaini to first-time visitors.<br/><br/>
        
        <b>Key Sections:</b><br/>
        <b>1. Header & Navigation</b> - The sticky top navigation bar with links to all major sections (Home, About Us, Our Programs, Our Impact, Get Involved, Contact Us) 
        and the prominent "GIVE HOPE" call-to-action button. The logo at the top left links back to the home page.<br/><br/>
        
        <b>2. Hero Section</b> - Eye-catching banner with rotating background images, welcoming headline, and a brief mission statement. 
        Creates a powerful first impression of the organization's purpose and visual identity.<br/><br/>
        
        <b>3. About Us Section</b> - Introduces the organization's core mission with a powerful quote: "Angaza Tumaini is committed to manifesting 
        the hope of Christ in tangible, practical ways, restoring dignity and purpose to those we serve." Meet Our Team subsection features detailed 
        profiles of founders Erick and Krista Baraza, and team members Evans Wandera, Jackline Mueni, Felix Mito, Naureen Mugeni, and Benard Owira. 
        Each profile includes a photo, role, biography, and inspiring biblical quote.<br/><br/>
        
        <b>4. Our Programs Section</b> - Displays five program cards with icons, titles, and descriptions: FAITH Program, Education Program, 
        Life-skills Program, Socio-economic Empowerment, and Community Outreach. Each card has a "Learn more" link for deeper information. 
        A sixth card invites visitors to "Give Hope" by donating.<br/><br/>
        
        <b>5. Our Impact in Numbers</b> - Animated counters displaying key metrics (e.g., "X Children Served", "Y Lives Changed", "Z Years of Service") 
        to visually communicate organizational reach and effectiveness.<br/><br/>
        
        <b>6. Get Involved Section</b> - Explains various ways to support the mission: Volunteer, Partner/Corporate Support, Sponsor a Child, 
        Donate, and Subscribe to Newsletter. Each option has a descriptive paragraph and a call-to-action button.<br/><br/>
        
        <b>7. Contact Section</b> - Contact form (powered by Formspree) for inquiries, with fields for Name, Email, Subject, and Message. 
        Displays contact information (email, phone, WhatsApp) and location details.<br/><br/>
        
        <b>8. Footer</b> - Contains social media icons (circular buttons for Facebook, Instagram, Gmail, TikTok, WhatsApp), quick links to all pages, 
        organization info, and a newsletter subscription call-to-action "JOIN OUR NEWSLETTER" linking to the Newsletter page.<br/><br/>
        
        <b>How to Use:</b> Scroll through to get a complete overview. Click on "Learn more" links to dive deeper into specific programs. 
        Use the navigation bar to jump to specific sections. Click "GIVE HOPE" or any "Donate" button to support the organization.
        """,
        body_style
    ))
    
    story.append(Spacer(1, 0.15*inch))
    
    # Contact Page
    story.append(Paragraph("<b>CONTACT PAGE (contact.html)</b>", subheading_style))
    story.append(Paragraph(
        """<b>What You'll Find:</b> A dedicated contact and communication page for reaching out to Angaza Tumaini.<br/><br/>
        
        <b>Key Sections:</b><br/>
        <b>1. Contact Hero</b> - Professional header section with gradient background, welcoming visitors and explaining the purpose of the page.<br/><br/>
        
        <b>2. Contact Form</b> - Integrated form (Formspree backend) with fields for:<br/>
        • Full Name (required)<br/>
        • Email Address (required)<br/>
        • Subject Line (required)<br/>
        • Message/Comment (required)<br/>
        A submit button sends the message directly to AngazaTumaini.org@gmail.com<br/><br/>
        
        <b>3. Contact Information Cards</b> - Beautiful glass-effect cards displaying:<br/>
        • Email: AngazaTumaini.org@gmail.com (clickable mailto: link with Gmail fallback)<br/>
        • Phone: +254 716 475764 (clickable tel: link)<br/>
        • WhatsApp: https://wa.link/xjt1s4 (opens WhatsApp chat)<br/>
        • Address: Olympic Estate, Kibera, Nairobi, Kenya<br/><br/>
        
        <b>4. Social Media Links</b> - Circular icon buttons linking to Facebook, Instagram, TikTok, and other social channels.<br/><br/>
        
        <b>How to Use:</b> Fill out the contact form for general inquiries. Call +254 716 475764 for immediate contact. 
        Use WhatsApp (https://wa.link/xjt1s4) for quick messaging. Follow on social media for updates.
        """,
        body_style
    ))
    
    story.append(Spacer(1, 0.15*inch))
    
    # Newsletter Page
    story.append(Paragraph("<b>NEWSLETTER & SOCIALS PAGE (newsletter.html)</b>", subheading_style))
    story.append(Paragraph(
        """<b>What You'll Find:</b> A dedicated page for newsletter subscription and social media engagement.<br/><br/>
        
        <b>Key Sections:</b><br/>
        <b>1. Newsletter Signup</b> - Encouraging visitors to stay updated with:<br/>
        • Email subscription form (mailto: link to subscribe)<br/>
        • Description of newsletter content: programs, events, and impact stories<br/><br/>
        
        <b>2. Follow Us Section</b> - Social media icons and links to:<br/>
        • Facebook - https://www.facebook.com/profile.php?id=61552268876833<br/>
        • Instagram - Official account<br/>
        • TikTok - Video content<br/>
        • Gmail - AngazaTumaini.org@gmail.com<br/>
        • WhatsApp - https://wa.link/xjt1s4<br/><br/>
        
        <b>3. Share Buttons</b> - Easy sharing of content to your personal networks.<br/><br/>
        
        <b>How to Use:</b> Enter your email to subscribe to the newsletter. Click social icons to follow on each platform. 
        Share content with your network using the share buttons.
        """,
        body_style
    ))
    
    story.append(PageBreak())
    
    # ===== 7. CONTACT & SUPPORT =====
    story.append(Paragraph("7. Contact & Support Information", heading_style))
    story.append(Spacer(1, 0.15*inch))
    
    contact_data = [
        ['Communication Method', 'Details', 'Best For'],
        ['Email', 'AngazaTumaini.org@gmail.com', 'Detailed inquiries, applications'],
        ['Phone Call', '+254 716 475764', 'Urgent matters, immediate conversation'],
        ['WhatsApp', 'https://wa.link/xjt1s4', 'Quick messages, group inquiries'],
        ['Facebook', 'https://www.facebook.com/profile.php?id=61552268876833', 'Updates, community engagement'],
        ['Contact Form', 'Website contact page', 'General inquiries'],
        ['In-Person', 'Olympic Estate, Kibera, Nairobi', 'Volunteer intake, visits'],
    ]
    
    contact_table = Table(contact_data, colWidths=[1.5*inch, 2.5*inch, 1.8*inch])
    contact_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), SECONDARY_COLOR),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), white),
        ('GRID', (0, 0), (-1, -1), 1, HexColor('#D1D5DB')),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ]))
    story.append(contact_table)
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(
        "<b>Response Time:</b> We aim to respond to all inquiries within 24-48 hours. For urgent matters, please call or use WhatsApp.",
        light_body
    ))
    
    story.append(PageBreak())
    
    # ===== 8. FAQ =====
    story.append(Paragraph("8. Frequently Asked Questions (FAQ)", heading_style))
    story.append(Spacer(1, 0.15*inch))
    
    faqs = [
        ("What is Angaza Tumaini Mission Center?", 
         "Angaza Tumaini is a Christian community-based ministry in Kibera, Nairobi, dedicated to serving children, youth, and families through five core programs: Faith Formation, Education, Life-Skills, Socio-economic Empowerment, and Community Outreach."),
        
        ("When was the organization founded?", 
         "Angaza Tumaini was founded by Erick and Krista Baraza. The website was launched on October 11, 2025."),
        
        ("Where is Angaza Tumaini located?", 
         "We are located in Olympic Estate, Kibera, Nairobi, Kenya – one of the most underserved areas of Nairobi."),
        
        ("How can I support Angaza Tumaini?", 
         "You can support us by: (1) Making a financial donation, (2) Volunteering your time and skills, (3) Becoming a corporate partner, (4) Sponsoring a child, (5) Subscribing to our newsletter, or (6) Sharing our work with others."),
        
        ("How can I volunteer?", 
         "To volunteer, contact us via email (AngazaTumaini.org@gmail.com), phone (+254 716 475764), or WhatsApp (https://wa.link/xjt1s4). We welcome volunteers in education, mentoring, healthcare, skilled trades, and general support."),
        
        ("What are the hours of operation?", 
         "For specific hours and program schedules, please contact us directly at AngazaTumaini.org@gmail.com or +254 716 475764."),
        
        ("Can I sponsor a child?", 
         "Yes! Child sponsorship is one of our programs. Contact us to discuss sponsorship opportunities and how you can support a child's education, meals, and spiritual development."),
        
        ("How is my donation used?", 
         "Donations go directly to supporting our five core programs: spiritual formation, academic tutoring, life-skills training, livelihood support, and community outreach initiatives. We maintain financial transparency and accountability."),
        
        ("Is there a newsletter I can subscribe to?", 
         "Yes! Visit our Newsletter page or click 'JOIN OUR NEWSLETTER' in the footer to stay updated on our programs, events, and impact stories."),
        
        ("How do I report a concern or feedback?", 
         "We welcome feedback! Use the contact form on our Contact page, email us, or call us directly. Your feedback helps us improve our services."),
    ]
    
    for i, (question, answer) in enumerate(faqs, 1):
        story.append(Paragraph(f"<b>Q{i}: {question}</b>", subheading_style))
        story.append(Paragraph(f"<b>A:</b> {answer}", body_style))
        story.append(Spacer(1, 0.1*inch))
    
    story.append(PageBreak())
    
    # ===== 9. WAYS TO GET INVOLVED =====
    story.append(Paragraph("9. Getting Involved — Ways to Support", heading_style))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph(
        "There are many meaningful ways to make a difference in the lives of children and families in Kibera. Below are the main avenues for support:",
        body_style
    ))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("<b>1. 💰 Make a Financial Donation</b>", subheading_style))
    story.append(Paragraph(
        """Support our programs through financial contributions. Every shilling helps us provide:<br/>
        • Meals and nutrition for children<br/>
        • Educational materials and tutoring<br/>
        • Vocational training equipment<br/>
        • Medical supplies and health services<br/>
        • Program materials and supplies<br/><br/>
        You can donate through the "GIVE HOPE" button on our website or contact us for payment instructions.
        """,
        body_style
    ))
    
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph("<b>2. 🤝 Volunteer Your Time & Skills</b>", subheading_style))
    story.append(Paragraph(
        """Volunteer in areas such as:<br/>
        • Education tutoring (Math, English, Science)<br/>
        • Faith/discipleship mentoring<br/>
        • Healthcare and hygiene education<br/>
        • Skills training (tailoring, carpentry, welding)<br/>
        • Organizational support and administration<br/>
        • Community outreach and service<br/><br/>
        Contact us to discuss volunteer opportunities that match your skills and availability.
        """,
        body_style
    ))
    
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph("<b>3. 🏢 Corporate & Institutional Partnerships</b>", subheading_style))
    story.append(Paragraph(
        """Businesses and organizations can partner with us through:<br/>
        • In-kind donations (educational materials, food, equipment)<br/>
        • Corporate volunteering and team service days<br/>
        • Sponsorship of programs or events<br/>
        • Internship and job placement opportunities for our youth<br/><br/>
        Contact us to explore partnership opportunities.
        """,
        body_style
    ))
    
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph("<b>4. 👦 Sponsor a Child</b>", subheading_style))
    story.append(Paragraph(
        """Make a long-term impact by becoming a child sponsor. Your sponsorship provides:<br/>
        • Education and tutoring support<br/>
        • Daily meals and nutrition<br/>
        • School supplies and materials<br/>
        • Health services and medical support<br/>
        • Spiritual mentorship and guidance<br/><br/>
        Connect with a child and be part of their journey to hope and success.
        """,
        body_style
    ))
    
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph("<b>5. 📧 Stay Connected & Share</b>", subheading_style))
    story.append(Paragraph(
        """• Subscribe to our newsletter for updates<br/>
        • Follow us on Facebook, Instagram, and TikTok<br/>
        • Share our story with your network<br/>
        • Pray for our mission and community<br/>
        • Advocate for social justice and community development
        """,
        body_style
    ))
    
    story.append(PageBreak())
    
    # ===== 10. TECHNICAL DETAILS =====
    story.append(Paragraph("10. Technical Details & Accessibility", heading_style))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("<b>Website Technology & Platform</b>", subheading_style))
    
    tech_data = [
        ['Component', 'Technology', 'Purpose'],
        ['Frontend', 'HTML5, CSS3, Tailwind CSS', 'Modern, responsive user interface'],
        ['Styling', 'Custom CSS, Tailwind Framework', 'Professional, consistent design'],
        ['Icons', 'Lucide Icons + PNG Images', 'Visual communication'],
        ['Fonts', 'Poppins (headings), Inter (body)', 'Modern, readable typography'],
        ['Contact Form', 'Formspree Backend', 'Email form submissions'],
        ['Hosting', 'Vercel', 'Fast, reliable static hosting'],
        ['Version Control', 'GitHub', 'Source code management'],
        ['Launch Date', 'October 11, 2025', 'Website live date'],
    ]
    
    tech_table = Table(tech_data, colWidths=[1.5*inch, 2*inch, 2.5*inch])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY_COLOR),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), white),
        ('GRID', (0, 0), (-1, -1), 1, HexColor('#D1D5DB')),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ]))
    story.append(tech_table)
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("<b>Accessibility Features</b>", subheading_style))
    story.append(Paragraph(
        """Our website is designed to be accessible to all users, including those with disabilities:<br/><br/>
        ✓ <b>Responsive Design:</b> Works perfectly on all device sizes (mobile, tablet, desktop)<br/>
        ✓ <b>Clear Navigation:</b> Intuitive menu structure with keyboard navigation support<br/>
        ✓ <b>Readable Typography:</b> Clear fonts with good contrast ratios for readability<br/>
        ✓ <b>Alt Text:</b> All images have descriptive alt text for screen readers<br/>
        ✓ <b>Color Accessibility:</b> Color choices meet WCAG accessibility standards<br/>
        ✓ <b>Fast Loading:</b> Optimized images and code for quick page loads<br/>
        ✓ <b>Mobile-Friendly:</b> Touch-friendly buttons and links for mobile users<br/>
        ✓ <b>Semantic HTML:</b> Proper use of HTML structure for assistive technologies
        """,
        body_style
    ))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("<b>Browser Compatibility</b>", subheading_style))
    story.append(Paragraph(
        """The website works best on modern browsers including:<br/>
        • Chrome/Chromium (latest version)<br/>
        • Firefox (latest version)<br/>
        • Safari (latest version)<br/>
        • Edge (latest version)<br/>
        • Mobile browsers (Chrome, Safari, Firefox)<br/><br/>
        <b>Note:</b> For the best experience, keep your browser updated to the latest version.
        """,
        body_style
    ))
    
    story.append(PageBreak())
    
    # ===== CLOSING =====
    story.append(Spacer(1, 1*inch))
    
    story.append(Paragraph("Thank You for Your Interest!", title_style))
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph(
        """We are grateful for every person who takes time to learn about Angaza Tumaini's mission and consider how they might support our work. 
        Whether through prayer, volunteering, donation, or simply sharing our story with others, your involvement makes a real difference in the 
        lives of children and families in Kibera.<br/><br/>
        
        At Angaza Tumaini, we believe that every child has God-given potential and deserves hope, dignity, and opportunity. Together, 
        we are shining the light of Christ in one of the most underserved areas of Nairobi.<br/><br/>
        
        <b>For more information or to get involved, please reach out:</b><br/>
        Email: AngazaTumaini.org@gmail.com<br/>
        Phone: +254 716 475764<br/>
        WhatsApp: https://wa.link/xjt1s4<br/>
        Website: https://angaza-tumaini-o4nwg3zz9-calvin-wanyamas-projects.vercel.app<br/><br/>
        
        <i>"Let your light shine before others, that they may see your good deeds and glorify your Father in heaven." – Matthew 5:16</i>
        """,
        body_style
    ))
    
    story.append(Spacer(1, 0.5*inch))
    
    story.append(Paragraph(
        "© 2025 Angaza Tumaini Mission Center. All rights reserved. Powered by faith, love, and the hope of Christ.",
        ParagraphStyle(
            'Footer',
            parent=styles['Normal'],
            fontSize=9,
            textColor=TEXT_COLOR,
            alignment=1,
            fontName='Helvetica-Oblique'
        )
    ))
    
    # Build PDF
    doc.build(story)
    print(f"✅ Comprehensive User Manual created: {filename}")
    print(f"   📄 Pages: Multiple (detailed manual with FAQ, team profiles, and program descriptions)")
    print(f"   📋 Sections: 10 major sections covering all website pages and organizational details")
    print(f"   🎨 Style: Modern & Classic with professional typography and color scheme")

if __name__ == "__main__":
    create_manual()
