import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.lib.units import inch, cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

# Register fonts
pdfmetrics.registerFont(TTFont('Times New Roman', '/usr/share/fonts/truetype/english/Times-New-Roman.ttf'))
pdfmetrics.registerFont(TTFont('Calibri', '/usr/share/fonts/truetype/english/calibri-regular.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSans', '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'))
registerFontFamily('Times New Roman', normal='Times New Roman', bold='Times New Roman')
registerFontFamily('Calibri', normal='Calibri', bold='Calibri')

pdf_filename = "FounderGrid_Business_Improvement_Plan.pdf"
pdf_path = os.path.join("/home/z/my-project/download", pdf_filename)

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    title="FounderGrid_Business_Improvement_Plan",
    author='Z.ai',
    creator='Z.ai',
    subject='Comprehensive business improvement plan for FounderGrid digital products platform',
    leftMargin=1*inch,
    rightMargin=1*inch,
    topMargin=0.8*inch,
    bottomMargin=0.8*inch,
)

# Colors
EMERALD = colors.HexColor('#059669')
DARK_SLATE = colors.HexColor('#1E293B')
TABLE_HEADER = colors.HexColor('#1F4E79')
TABLE_ODD = colors.HexColor('#F5F5F5')
ACCENT = colors.HexColor('#059669')

# Styles
cover_title = ParagraphStyle(
    name='CoverTitle', fontName='Times New Roman', fontSize=38,
    leading=46, alignment=TA_CENTER, spaceAfter=24, textColor=DARK_SLATE
)
cover_subtitle = ParagraphStyle(
    name='CoverSubtitle', fontName='Times New Roman', fontSize=18,
    leading=26, alignment=TA_CENTER, spaceAfter=12, textColor=colors.HexColor('#475569')
)
cover_info = ParagraphStyle(
    name='CoverInfo', fontName='Times New Roman', fontSize=13,
    leading=20, alignment=TA_CENTER, spaceAfter=8, textColor=colors.HexColor('#64748B')
)
h1_style = ParagraphStyle(
    name='H1', fontName='Times New Roman', fontSize=20,
    leading=28, spaceBefore=18, spaceAfter=10, textColor=DARK_SLATE
)
h2_style = ParagraphStyle(
    name='H2', fontName='Times New Roman', fontSize=15,
    leading=22, spaceBefore=14, spaceAfter=8, textColor=colors.HexColor('#334155')
)
h3_style = ParagraphStyle(
    name='H3', fontName='Times New Roman', fontSize=12,
    leading=18, spaceBefore=10, spaceAfter=6, textColor=colors.HexColor('#475569')
)
body_style = ParagraphStyle(
    name='Body', fontName='Times New Roman', fontSize=10.5,
    leading=17, alignment=TA_JUSTIFY, spaceAfter=6
)
bullet_style = ParagraphStyle(
    name='Bullet', fontName='Times New Roman', fontSize=10.5,
    leading=17, alignment=TA_LEFT, leftIndent=20, spaceAfter=4,
    bulletIndent=8, bulletFontSize=10.5
)
header_cell = ParagraphStyle(
    name='HeaderCell', fontName='Times New Roman', fontSize=10,
    leading=14, textColor=colors.white, alignment=TA_CENTER
)
cell_style = ParagraphStyle(
    name='Cell', fontName='Times New Roman', fontSize=9.5,
    leading=14, textColor=colors.black, alignment=TA_CENTER
)
cell_left = ParagraphStyle(
    name='CellLeft', fontName='Times New Roman', fontSize=9.5,
    leading=14, textColor=colors.black, alignment=TA_LEFT
)
cell_justify = ParagraphStyle(
    name='CellJustify', fontName='Times New Roman', fontSize=9.5,
    leading=14, textColor=colors.black, alignment=TA_JUSTIFY
)
caption_style = ParagraphStyle(
    name='Caption', fontName='Times New Roman', fontSize=9,
    leading=14, alignment=TA_CENTER, textColor=colors.HexColor('#64748B'),
    spaceBefore=3, spaceAfter=6
)

story = []

# COVER PAGE
story.append(Spacer(1, 100))
story.append(Paragraph('<b>FounderGrid</b>', cover_title))
story.append(Spacer(1, 12))
story.append(Paragraph('<b>Business Improvement Plan</b>', cover_subtitle))
story.append(Spacer(1, 36))

cover_line_data = [[Paragraph('', cell_style)]]
cover_line = Table(cover_line_data, colWidths=[3*inch])
cover_line.setStyle(TableStyle([
    ('LINEBELOW', (0, 0), (-1, -1), 2, EMERALD),
]))
story.append(cover_line)

story.append(Spacer(1, 36))
story.append(Paragraph('A Comprehensive Strategy for Building, Launching, and Scaling<br/>a Digital Products Business for Freelancers and Solopreneurs', cover_info))
story.append(Spacer(1, 60))
story.append(Paragraph('Prepared by Z.ai', cover_info))
story.append(Paragraph('April 2026', cover_info))
story.append(Paragraph('Confidential', cover_info))
story.append(PageBreak())

# TABLE OF CONTENTS (manual but clean)
story.append(Paragraph('<b>Table of Contents</b>', h1_style))
story.append(Spacer(1, 12))

toc_entries = [
    ('1.', 'Executive Summary', ''),
    ('2.', 'Market Analysis and Niche Strategy', ''),
    ('3.', 'Product Positioning and Pricing', ''),
    ('4.', 'Website and Conversion Strategy', ''),
    ('5.', 'Revenue Model Optimization', ''),
    ('6.', 'Customer Acquisition Strategy', ''),
    ('7.', 'Legal Protections and Compliance', ''),
    ('8.', 'Financial Projections', ''),
    ('9.', 'Competitive Analysis', ''),
    ('10.', 'Implementation Roadmap', ''),
    ('11.', 'Risk Assessment and Mitigation', ''),
    ('12.', 'Key Performance Indicators', ''),
]
toc_style = ParagraphStyle(
    name='TOC', fontName='Times New Roman', fontSize=11,
    leading=22, alignment=TA_LEFT
)
for num, title, _ in toc_entries:
    story.append(Paragraph(f'<b>{num}</b>  {title}', toc_style))

story.append(PageBreak())

# SECTION 1: EXECUTIVE SUMMARY
story.append(Paragraph('<b>1. Executive Summary</b>', h1_style))
story.append(Spacer(1, 6))
story.append(Paragraph(
    'FounderGrid is a digital products platform designed to equip freelancers, solopreneurs, and one-person '
    'businesses with the tools they need to compete effectively against larger competitors. The business model '
    'centers on selling high-value, immediately usable digital products including AI prompt libraries, business '
    'operations templates, and marketing strategy frameworks. Each product is delivered as a professional PDF '
    'with instant download capability, enabling a hands-off fulfillment process that scales without additional '
    'overhead or operational complexity.', body_style))
story.append(Paragraph(
    'The original business plan established a solid foundation: three well-structured products, a sole proprietor '
    'structure for minimum startup cost, and Stripe integration for professional payment processing. However, '
    'several critical gaps existed that would significantly limit growth potential. The products were positioned '
    'too generically for a saturated market, there was no customer acquisition strategy, the pricing model lacked '
    'a recurring revenue component, and no validation mechanism was in place to confirm market demand before '
    'investing heavily in development.', body_style))
story.append(Paragraph(
    'This improvement plan addresses every one of those gaps with specific, actionable recommendations. The '
    'core strategic shift is from a generic "sell to everyone" approach to a targeted "solve specific problems for '
    'freelancers and solopreneurs" positioning. This niche audience is large enough to sustain a profitable business '
    '(over 70 million freelancers in the US alone), desperate for time-saving solutions, and willing to pay for '
    'tools that deliver measurable results. The plan also introduces a lead magnet email capture system to build '
    'a customer pipeline before the first sale is made, and a subscription upsell path that transforms one-time '
    'buyers into recurring revenue streams.', body_style))

# SECTION 2: MARKET ANALYSIS
story.append(Spacer(1, 12))
story.append(Paragraph('<b>2. Market Analysis and Niche Strategy</b>', h1_style))
story.append(Spacer(1, 6))

story.append(Paragraph('<b>2.1 Why Freelancers and Solopreneurs?</b>', h2_style))
story.append(Paragraph(
    'The freelance economy has experienced explosive growth, accelerating significantly since 2020. In the United '
    'States alone, there are now over 70 million freelancers, representing approximately 36% of the total workforce. '
    'This figure is projected to exceed 50% by 2027 as remote work and digital entrepreneurship become increasingly '
    'mainstream. Globally, the freelance market is estimated at over $1.5 trillion and growing at a compound annual '
    'growth rate of 15%. These individuals face a unique set of challenges that make them ideal customers for '
    'digital productivity tools: they wear every hat in their business, have limited budgets compared to companies '
    'with teams, and are constantly searching for ways to do more with less time.', body_style))
story.append(Paragraph(
    'Unlike employees who have access to corporate tools, training programs, and specialized departments, freelancers '
    'must handle content creation, marketing, operations, finances, and customer service entirely on their own. This '
    'creates an intense demand for ready-made solutions that can be deployed immediately without a learning curve. '
    'A pre-built business template saves them dozens of hours of research and formatting. A curated AI prompt library '
    'eliminates the trial-and-error phase of learning to use AI tools effectively. A marketing playbook gives them a '
    'framework they can execute without hiring an agency at $3,000 to $10,000 per month.', body_style))

story.append(Paragraph('<b>2.2 Target Audience Segments</b>', h2_style))

audience_data = [
    [Paragraph('<b>Segment</b>', header_cell), Paragraph('<b>Size</b>', header_cell),
     Paragraph('<b>Pain Points</b>', header_cell), Paragraph('<b>Buying Power</b>', header_cell)],
    [Paragraph('Freelance Writers/Creators', cell_left), Paragraph('12M+', cell_style),
     Paragraph('Content production bottleneck, inconsistent output', cell_justify), Paragraph('$50-200/month', cell_style)],
    [Paragraph('Independent Consultants', cell_left), Paragraph('8M+', cell_style),
     Paragraph('No systems, reinventing processes', cell_justify), Paragraph('$100-500/month', cell_style)],
    [Paragraph('E-commerce Solopreneurs', cell_left), Paragraph('15M+', cell_style),
     Paragraph('Marketing overwhelm, no strategy', cell_justify), Paragraph('$50-300/month', cell_style)],
    [Paragraph('Coaches and Course Creators', cell_left), Paragraph('5M+', cell_style),
     Paragraph('Scaling content, lead generation', cell_justify), Paragraph('$100-500/month', cell_style)],
    [Paragraph('Agency Owners (1-5 people)', cell_left), Paragraph('3M+', cell_style),
     Paragraph('Client management, SOPs needed', cell_justify), Paragraph('$200-1000/month', cell_style)],
]
audience_table = Table(audience_data, colWidths=[1.6*inch, 0.8*inch, 2.5*inch, 1.3*inch])
audience_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BACKGROUND', (0, 1), (-1, 1), colors.white),
    ('BACKGROUND', (0, 2), (-1, 2), TABLE_ODD),
    ('BACKGROUND', (0, 3), (-1, 3), colors.white),
    ('BACKGROUND', (0, 4), (-1, 4), TABLE_ODD),
    ('BACKGROUND', (0, 5), (-1, 5), colors.white),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))
story.append(Spacer(1, 18))
story.append(audience_table)
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 1.</b> Target Audience Segments for FounderGrid Products', caption_style))
story.append(Spacer(1, 18))

story.append(Paragraph('<b>2.3 Competitive Landscape</b>', h2_style))
story.append(Paragraph(
    'The digital products market is undeniably crowded, with platforms like Etsy, Gumroad, and Creative Market hosting '
    'thousands of template and prompt products. However, the vast majority of these competitors suffer from three fatal '
    'flaws that create a significant opportunity for FounderGrid. First, most products are generic "500 ChatGPT prompts" '
    'bundles with no audience specificity, meaning they try to serve everyone and end up serving no one particularly well. '
    'Second, the quality is often poor, with products consisting of hastily compiled lists that provide minimal practical '
    'value. Third, there is rarely any follow-up value or community, resulting in a one-time transaction with no customer '
    'retention strategy.', body_style))
story.append(Paragraph(
    'FounderGrid differentiates itself by being explicitly built for a specific audience with specific problems. Every '
    'product is framed around the outcomes freelancers care about: saving time, looking professional, winning clients, '
    'and growing revenue. The brand identity reinforces this positioning through its name, messaging, and marketing. '
    'Additionally, the email capture and lead nurture system creates a relationship that extends far beyond the initial '
    'purchase, opening the door to upsells, subscriptions, and community memberships.', body_style))

# SECTION 3: PRODUCT POSITIONING
story.append(Spacer(1, 12))
story.append(Paragraph('<b>3. Product Positioning and Pricing</b>', h1_style))
story.append(Spacer(1, 6))

story.append(Paragraph('<b>3.1 Repositioned Product Lineup</b>', h2_style))
story.append(Paragraph(
    'Each product has been repositioned to speak directly to the target audience. The emphasis is on outcomes and '
    'transformations rather than features and counts. Customers do not buy "500 prompts"; they buy "10 extra hours '
    'per week." This reframing is critical for conversion, as it connects the product to the emotional and practical '
    'needs of the buyer rather than treating it as a commodity.', body_style))

product_data = [
    [Paragraph('<b>Product</b>', header_cell), Paragraph('<b>Price</b>', header_cell),
     Paragraph('<b>Target Outcome</b>', header_cell), Paragraph('<b>Format</b>', header_cell)],
    [Paragraph('AI Prompt Pack for Founders', cell_left), Paragraph('$49', cell_style),
     Paragraph('Save 10+ hours/week on content, emails, marketing', cell_justify), Paragraph('PDF Download', cell_style)],
    [Paragraph('Solo Ops Playbook', cell_left), Paragraph('$79', cell_style),
     Paragraph('Professional business systems in minutes, not months', cell_justify), Paragraph('PDF Download', cell_style)],
    [Paragraph('Launch Marketing Kit', cell_left), Paragraph('$99', cell_style),
     Paragraph('Launch campaigns without hiring an agency', cell_justify), Paragraph('PDF Download', cell_style)],
    [Paragraph('<b>All-Access Bundle</b>', cell_left), Paragraph('<b>$189</b>', cell_style),
     Paragraph('<b>Complete business toolkit, save $38</b>', cell_justify), Paragraph('<b>PDF Downloads</b>', cell_style)],
]
product_table = Table(product_data, colWidths=[1.7*inch, 0.7*inch, 2.6*inch, 1.2*inch])
product_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BACKGROUND', (0, 1), (-1, 1), colors.white),
    ('BACKGROUND', (0, 2), (-1, 2), TABLE_ODD),
    ('BACKGROUND', (0, 3), (-1, 3), colors.white),
    ('BACKGROUND', (0, 4), (-1, 4), colors.HexColor('#ECFDF5')),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))
story.append(Spacer(1, 18))
story.append(product_table)
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 2.</b> Repositioned Product Lineup with Outcome-Focused Messaging', caption_style))
story.append(Spacer(1, 18))

story.append(Paragraph('<b>3.2 Pricing Psychology and Strategy</b>', h2_style))
story.append(Paragraph(
    'The pricing strategy employs three well-established psychological principles to maximize conversions and average '
    'order value. The first is anchoring: by presenting the All-Access Bundle at $189 alongside individual products at '
    '$49, $79, and $99, the bundle appears as exceptional value, encouraging customers to spend more than they initially '
    'intended. Studies show that presenting a higher-priced option first increases the perceived value of mid-range '
    'options and shifts the average purchase upward by 20-40%.', body_style))
story.append(Paragraph(
    'The second principle is price ending. All prices end in 9, which has been demonstrated through extensive research '
    'to increase purchases by up to 24% compared to rounded numbers. The brain processes $49 as significantly less '
    'than $50, even though the difference is only one dollar. This is particularly effective for impulse purchases '
    'and first-time buyers who are still building trust with the brand.', body_style))
story.append(Paragraph(
    'The third principle is the decoy effect. The Solo Ops Playbook at $79 serves as a decoy that makes the $99 '
    'Launch Marketing Kit appear as a small incremental upgrade for significantly more value. Most customers will '
    'choose either the cheapest option (to minimize risk) or the most expensive option (to maximize value), with '
    'the middle option primarily serving to make the high-end option look more attractive.', body_style))

# SECTION 4: WEBSITE STRATEGY
story.append(Spacer(1, 12))
story.append(Paragraph('<b>4. Website and Conversion Strategy</b>', h1_style))
story.append(Spacer(1, 6))

story.append(Paragraph('<b>4.1 Landing Page Architecture</b>', h2_style))
story.append(Paragraph(
    'The landing page has been designed following proven conversion optimization principles from high-performing '
    'SaaS and digital product companies. Every section serves a specific psychological purpose in moving the visitor '
    'from awareness to interest to desire to action. The page begins with a hero section that immediately communicates '
    'the primary value proposition in language the target audience recognizes: "Stop Wasting Hours on Tasks AI Can Do '
    'in Seconds." This headline works because it identifies the problem, implies the solution, and speaks directly to '
    'the frustration the audience feels daily.', body_style))
story.append(Paragraph(
    'The pain points section that follows is strategically placed to build emotional resonance. When visitors see their '
    'exact frustrations articulated, they feel understood, which builds trust far more effectively than any testimonial. '
    'The products section then presents the solution with clear pricing, and the email capture lead magnet gives visitors '
    'a low-commitment way to engage with the brand before making a purchase decision. This is critical because most '
    'visitors will not buy on their first visit. The lead magnet captures their email, allowing automated follow-up '
    'sequences to nurture them toward a purchase over the following days and weeks.', body_style))

story.append(Paragraph('<b>4.2 Conversion Optimization Elements</b>', h2_style))

conversion_data = [
    [Paragraph('<b>Element</b>', header_cell), Paragraph('<b>Purpose</b>', header_cell),
     Paragraph('<b>Expected Impact</b>', header_cell)],
    [Paragraph('Lead magnet email capture', cell_left), Paragraph('Build email list from 2-5% of visitors', cell_justify),
     Paragraph('Pipeline for nurturing and conversion', cell_justify)],
    [Paragraph('Social proof line in hero', cell_left), Paragraph('Reduce skepticism immediately', cell_justify),
     Paragraph('15-25% increase in trust metrics', cell_justify)],
    [Paragraph('Outcome-focused product descriptions', cell_left), Paragraph('Connect product to customer goals', cell_justify),
     Paragraph('Higher perceived value, less price sensitivity', cell_justify)],
    [Paragraph('FAQ accordion section', cell_left), Paragraph('Remove objections before checkout', cell_justify),
     Paragraph('Reduce abandoned checkouts by 10-15%', cell_justify)],
    [Paragraph('Multiple CTA placements', cell_left), Paragraph('Capture intent at multiple decision points', cell_justify),
     Paragraph('20-30% increase in click-through rate', cell_justify)],
    [Paragraph('Bundle pricing with savings', cell_left), Paragraph('Increase average order value', cell_justify),
     Paragraph('Shift 30% of buyers to higher tier', cell_justify)],
]
conversion_table = Table(conversion_data, colWidths=[1.8*inch, 2.2*inch, 2.2*inch])
conversion_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BACKGROUND', (0, 1), (-1, 1), colors.white),
    ('BACKGROUND', (0, 2), (-1, 2), TABLE_ODD),
    ('BACKGROUND', (0, 3), (-1, 3), colors.white),
    ('BACKGROUND', (0, 4), (-1, 4), TABLE_ODD),
    ('BACKGROUND', (0, 5), (-1, 5), colors.white),
    ('BACKGROUND', (0, 6), (-1, 6), TABLE_ODD),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))
story.append(Spacer(1, 18))
story.append(conversion_table)
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 3.</b> Conversion Optimization Elements and Expected Impact', caption_style))
story.append(Spacer(1, 18))

# SECTION 5: REVENUE MODEL
story.append(Paragraph('<b>5. Revenue Model Optimization</b>', h1_style))
story.append(Spacer(1, 6))

story.append(Paragraph('<b>5.1 Current vs. Optimized Revenue Model</b>', h2_style))
story.append(Paragraph(
    'The original plan relied entirely on one-time product sales. While this generates revenue, it creates a feast-or-famine '
    'cycle where income depends entirely on acquiring new customers each month. The optimized model introduces multiple '
    'revenue streams that compound over time, creating a more stable and predictable business.', body_style))

revenue_data = [
    [Paragraph('<b>Revenue Stream</b>', header_cell), Paragraph('<b>Type</b>', header_cell),
     Paragraph('<b>Price Point</b>', header_cell), Paragraph('<b>Frequency</b>', header_cell),
     Paragraph('<b>Potential Monthly Revenue</b>', header_cell)],
    [Paragraph('Individual Products', cell_left), Paragraph('One-time', cell_style),
     Paragraph('$49-99', cell_style), Paragraph('Per sale', cell_style), Paragraph('$500-2,000', cell_style)],
    [Paragraph('All-Access Bundle', cell_left), Paragraph('One-time', cell_style),
     Paragraph('$189', cell_style), Paragraph('Per sale', cell_style), Paragraph('$500-1,500', cell_style)],
    [Paragraph('Monthly Prompt Updates', cell_left), Paragraph('Subscription', cell_style),
     Paragraph('$9.99/mo', cell_style), Paragraph('Monthly', cell_style), Paragraph('$300-1,200', cell_style)],
    [Paragraph('Expansion Packs', cell_left), Paragraph('One-time', cell_style),
     Paragraph('$19-29', cell_style), Paragraph('Quarterly', cell_style), Paragraph('$200-800', cell_style)],
    [Paragraph('Community Access', cell_left), Paragraph('Subscription', cell_style),
     Paragraph('$14.99/mo', cell_style), Paragraph('Monthly', cell_style), Paragraph('$200-600', cell_style)],
]
revenue_table = Table(revenue_data, colWidths=[1.4*inch, 0.9*inch, 0.9*inch, 0.9*inch, 1.6*inch])
revenue_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BACKGROUND', (0, 1), (-1, 1), colors.white),
    ('BACKGROUND', (0, 2), (-1, 2), TABLE_ODD),
    ('BACKGROUND', (0, 3), (-1, 3), colors.white),
    ('BACKGROUND', (0, 4), (-1, 4), TABLE_ODD),
    ('BACKGROUND', (0, 5), (-1, 5), colors.white),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))
story.append(Spacer(1, 18))
story.append(revenue_table)
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 4.</b> Revenue Streams and Monthly Potential (6-12 Month Projections)', caption_style))
story.append(Spacer(1, 18))

story.append(Paragraph('<b>5.2 Customer Lifetime Value Analysis</b>', h2_style))
story.append(Paragraph(
    'The subscription model fundamentally changes the economics of the business. Under the original one-time-only '
    'model, each customer generates $49 to $189 and then the relationship ends. With subscriptions, a single customer '
    'who subscribes to monthly prompt updates at $9.99 per month generates $119.88 per year, and if they stay for '
    'three years (which is typical for high-quality subscription products), that single customer generates $359.64 '
    'in lifetime revenue. Add the initial product purchase of $189, and the customer lifetime value reaches $548.64, '
    'nearly three times the original one-time purchase amount.', body_style))
story.append(Paragraph(
    'The community membership tier at $14.99 per month further amplifies this effect. Members who join the community '
    'become invested in the brand ecosystem, making them significantly less likely to churn. Community members also '
    'become natural advocates who refer new customers, creating an organic growth loop that reduces customer '
    'acquisition costs over time. Even if only 10-15% of initial buyers convert to subscribers, this creates a '
    'meaningful recurring revenue floor that provides stability and predictability.', body_style))

# SECTION 6: CUSTOMER ACQUISITION
story.append(Spacer(1, 12))
story.append(Paragraph('<b>6. Customer Acquisition Strategy</b>', h1_style))
story.append(Spacer(1, 6))

story.append(Paragraph('<b>6.1 Free Traffic Channels</b>', h2_style))

traffic_data = [
    [Paragraph('<b>Channel</b>', header_cell), Paragraph('<b>Strategy</b>', header_cell),
     Paragraph('<b>Time Investment</b>', header_cell), Paragraph('<b>Expected Results</b>', header_cell)],
    [Paragraph('Pinterest', cell_left), Paragraph('Create infographics from templates, link to products', cell_justify),
     Paragraph('3-5 hours/week', cell_style), Paragraph('200-500 monthly visitors after 2 months', cell_justify)],
    [Paragraph('TikTok/Reels', cell_left), Paragraph('Short videos showing time savings with products', cell_justify),
     Paragraph('5-8 hours/week', cell_style), Paragraph('1,000-5,000 monthly visitors after 3 months', cell_justify)],
    [Paragraph('Reddit', cell_left), Paragraph('Share helpful prompts, build credibility', cell_justify),
     Paragraph('2-3 hours/week', cell_style), Paragraph('100-300 monthly visitors, high intent', cell_justify)],
    [Paragraph('SEO Blog', cell_left), Paragraph('Target long-tail keywords for freelancers', cell_justify),
     Paragraph('5-10 hours/week', cell_style), Paragraph('500-2,000 monthly visitors after 4 months', cell_justify)],
    [Paragraph('Product Hunt', cell_left), Paragraph('Launch day blitz with community support', cell_justify),
     Paragraph('One-time effort', cell_style), Paragraph('2,000-10,000 visitors in launch week', cell_justify)],
]
traffic_table = Table(traffic_data, colWidths=[1.1*inch, 2.1*inch, 1.2*inch, 2*inch])
traffic_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BACKGROUND', (0, 1), (-1, 1), colors.white),
    ('BACKGROUND', (0, 2), (-1, 2), TABLE_ODD),
    ('BACKGROUND', (0, 3), (-1, 3), colors.white),
    ('BACKGROUND', (0, 4), (-1, 4), TABLE_ODD),
    ('BACKGROUND', (0, 5), (-1, 5), colors.white),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))
story.append(Spacer(1, 18))
story.append(traffic_table)
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 5.</b> Free Traffic Channel Strategy and Expected Results', caption_style))
story.append(Spacer(1, 18))

story.append(Paragraph('<b>6.2 Email Nurture Sequence</b>', h2_style))
story.append(Paragraph(
    'The email nurture sequence is the most important customer acquisition tool after the landing page itself. '
    'Research from the Direct Marketing Association shows that email marketing generates an average return of $42 '
    'for every $1 spent, making it the highest-ROI marketing channel available. The sequence begins immediately after '
    'a visitor downloads the free lead magnet and consists of seven carefully timed emails over 14 days.', body_style))

email_data = [
    [Paragraph('<b>Day</b>', header_cell), Paragraph('<b>Email</b>', header_cell),
     Paragraph('<b>Content</b>', header_cell), Paragraph('<b>Goal</b>', header_cell)],
    [Paragraph('0', cell_style), Paragraph('Welcome + Deliver Lead Magnet', cell_left),
     Paragraph('Deliver the free PDF, introduce FounderGrid mission', cell_justify), Paragraph('Deliver value, set expectations', cell_justify)],
    [Paragraph('2', cell_style), Paragraph('Quick Win', cell_left),
     Paragraph('Share one powerful AI prompt with results', cell_justify), Paragraph('Demonstrate product quality', cell_justify)],
    [Paragraph('4', cell_style), Paragraph('Story + Social Proof', cell_left),
     Paragraph('Share customer success story with specifics', cell_justify), Paragraph('Build trust through evidence', cell_justify)],
    [Paragraph('7', cell_style), Paragraph('Educational', cell_left),
     Paragraph('Teach something valuable about AI/business', cell_justify), Paragraph('Position as authority', cell_justify)],
    [Paragraph('10', cell_style), Paragraph('Soft Pitch', cell_left),
     Paragraph('Introduce products as solution to discussed problems', cell_justify), Paragraph('Generate interest without pressure', cell_justify)],
    [Paragraph('12', cell_style), Paragraph('Hard Pitch + Bonus', cell_left),
     Paragraph('Offer products with time-limited bonus', cell_justify), Paragraph('Drive conversion with urgency', cell_justify)],
    [Paragraph('14', cell_style), Paragraph('Final Reminder', cell_left),
     Paragraph('Last chance for bonus, reset to nurture', cell_justify), Paragraph('Capture remaining conversions', cell_justify)],
]
email_table = Table(email_data, colWidths=[0.5*inch, 1.5*inch, 2.3*inch, 2*inch])
email_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BACKGROUND', (0, 1), (-1, 1), colors.white),
    ('BACKGROUND', (0, 2), (-1, 2), TABLE_ODD),
    ('BACKGROUND', (0, 3), (-1, 3), colors.white),
    ('BACKGROUND', (0, 4), (-1, 4), TABLE_ODD),
    ('BACKGROUND', (0, 5), (-1, 5), colors.white),
    ('BACKGROUND', (0, 6), (-1, 6), TABLE_ODD),
    ('BACKGROUND', (0, 7), (-1, 7), colors.white),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))
story.append(Spacer(1, 18))
story.append(email_table)
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 6.</b> 14-Day Email Nurture Sequence', caption_style))
story.append(Spacer(1, 18))

# SECTION 7: LEGAL
story.append(Paragraph('<b>7. Legal Protections and Compliance</b>', h1_style))
story.append(Spacer(1, 6))
story.append(Paragraph(
    'Operating as a sole proprietor provides maximum flexibility and zero startup cost, but it also means the founder '
    'assumes personal liability for business obligations. For a low-risk digital products business with no physical '
    'inventory, no employees, and no client-facing services that could cause physical harm, this risk is manageable. '
    'However, certain protections should be implemented from day one to minimize exposure and demonstrate '
    'professionalism to customers.', body_style))

legal_data = [
    [Paragraph('<b>Protection</b>', header_cell), Paragraph('<b>Purpose</b>', header_cell),
     Paragraph('<b>Cost</b>', header_cell), Paragraph('<b>Priority</b>', header_cell)],
    [Paragraph('Terms of Service', cell_left), Paragraph('Limit liability, define usage rights', cell_justify),
     Paragraph('Free (self-drafted)', cell_style), Paragraph('Immediate (Day 1)', cell_style)],
    [Paragraph('Privacy Policy', cell_left), Paragraph('Legal compliance with data laws', cell_justify),
     Paragraph('Free (self-drafted)', cell_style), Paragraph('Immediate (Day 1)', cell_style)],
    [Paragraph('Refund Policy', cell_left), Paragraph('Reduce chargebacks, build trust', cell_justify),
     Paragraph('Free (self-drafted)', cell_style), Paragraph('Immediate (Day 1)', cell_style)],
    [Paragraph('Disclaimer', cell_left), Paragraph('Protect against misuse claims', cell_justify),
     Paragraph('Free (self-drafted)', cell_style), Paragraph('Immediate (Day 1)', cell_style)],
    [Paragraph('Copyright Notice', cell_left), Paragraph('Protect product IP', cell_justify),
     Paragraph('Free (automatic)', cell_style), Paragraph('Immediate (Day 1)', cell_style)],
    [Paragraph('EULA', cell_left), Paragraph('Restrict redistribution', cell_justify),
     Paragraph('Free (self-drafted)', cell_style), Paragraph('Before first sale', cell_style)],
    [Paragraph('Business Name Registration', cell_left), Paragraph('Protect name in state', cell_justify),
     Paragraph('$50-150', cell_style), Paragraph('After first $500 revenue', cell_style)],
    [Paragraph('LLC Formation', cell_left), Paragraph('Shield personal assets', cell_justify),
     Paragraph('$50-300', cell_style), Paragraph('After first $2,000/month', cell_style)],
    [Paragraph('Trademark', cell_left), Paragraph('National brand protection', cell_justify),
     Paragraph('$250-750', cell_style), Paragraph('After $5,000/month', cell_style)],
]
legal_table = Table(legal_data, colWidths=[1.5*inch, 2*inch, 1.2*inch, 1.5*inch])
legal_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    *[('BACKGROUND', (0, i), (-1, i), colors.white if i % 2 == 1 else TABLE_ODD) for i in range(1, 10)],
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))
story.append(Spacer(1, 18))
story.append(legal_table)
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 7.</b> Legal Protections Roadmap by Priority and Revenue Milestone', caption_style))
story.append(Spacer(1, 18))

# SECTION 8: FINANCIAL PROJECTIONS
story.append(Paragraph('<b>8. Financial Projections</b>', h1_style))
story.append(Spacer(1, 6))
story.append(Paragraph(
    'The following projections are based on conservative estimates assuming steady implementation of the marketing '
    'strategy described in this plan. These figures assume no paid advertising until month four, relying entirely on '
    'organic traffic, email marketing, and social media content during the initial growth phase. The "pessimistic" '
    'scenario assumes only 50% of target traffic is achieved, while the "optimistic" scenario assumes the marketing '
    'strategy exceeds expectations by 50%.', body_style))

financial_data = [
    [Paragraph('<b>Metric</b>', header_cell), Paragraph('<b>Month 1-3</b>', header_cell),
     Paragraph('<b>Month 4-6</b>', header_cell), Paragraph('<b>Month 7-12</b>', header_cell)],
    [Paragraph('Monthly Visitors', cell_left), Paragraph('200-500', cell_style),
     Paragraph('1,000-3,000', cell_style), Paragraph('5,000-15,000', cell_style)],
    [Paragraph('Email Subscribers', cell_left), Paragraph('50-200', cell_style),
     Paragraph('300-1,000', cell_style), Paragraph('1,500-5,000', cell_style)],
    [Paragraph('Conversion Rate', cell_left), Paragraph('1-2%', cell_style),
     Paragraph('2-3%', cell_style), Paragraph('2-4%', cell_style)],
    [Paragraph('Monthly Revenue', cell_left), Paragraph('$100-500', cell_style),
     Paragraph('$500-2,500', cell_style), Paragraph('$2,000-8,000', cell_style)],
    [Paragraph('Monthly Costs', cell_left), Paragraph('$0-30', cell_style),
     Paragraph('$30-200', cell_style), Paragraph('$100-500', cell_style)],
    [Paragraph('Net Monthly Profit', cell_left), Paragraph('$70-470', cell_style),
     Paragraph('$300-2,300', cell_style), Paragraph('$1,500-7,500', cell_style)],
    [Paragraph('Cumulative Revenue', cell_left), Paragraph('$300-1,500', cell_style),
     Paragraph('$2,000-6,000', cell_style), Paragraph('$15,000-50,000', cell_style)],
]
financial_table = Table(financial_data, colWidths=[1.5*inch, 1.3*inch, 1.3*inch, 1.5*inch])
financial_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    *[('BACKGROUND', (0, i), (-1, i), colors.white if i % 2 == 1 else TABLE_ODD) for i in range(1, 8)],
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))
story.append(Spacer(1, 18))
story.append(financial_table)
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 8.</b> Financial Projections (Conservative Estimates, 12-Month Horizon)', caption_style))
story.append(Spacer(1, 18))

# SECTION 9: COMPETITIVE ANALYSIS
story.append(Paragraph('<b>9. Competitive Analysis</b>', h1_style))
story.append(Spacer(1, 6))
story.append(Paragraph(
    'Understanding the competitive landscape is essential for positioning FounderGrid effectively. The digital products '
    'market has several categories of competitors, each with distinct strengths and weaknesses. By analyzing these '
    'competitors systematically, FounderGrid can identify positioning gaps and develop differentiation strategies '
    'that create a sustainable competitive advantage.', body_style))

comp_data = [
    [Paragraph('<b>Competitor Type</b>', header_cell), Paragraph('<b>Examples</b>', header_cell),
     Paragraph('<b>Strengths</b>', header_cell), Paragraph('<b>Weaknesses</b>', header_cell),
     Paragraph('<b>FounderGrid Advantage</b>', header_cell)],
    [Paragraph('Marketplace Sellers', cell_left), Paragraph('Etsy, Gumroad', cell_style),
     Paragraph('Large audiences, easy discovery', cell_justify), Paragraph('Generic products, no brand, no support', cell_justify),
     Paragraph('Targeted niche, professional brand, email nurture', cell_justify)],
    [Paragraph('SaaS Template Companies', cell_left), Paragraph('Canva, Notion', cell_style),
     Paragraph('Polished products, trusted brands', cell_justify), Paragraph('Subscription required, limited customization', cell_justify),
     Paragraph('One-time purchase, fully customizable PDFs', cell_justify)],
    [Paragraph('AI Prompt Marketplaces', cell_left), Paragraph('PromptBase', cell_style),
     Paragraph('Specialized in AI prompts', cell_justify), Paragraph('Per-prompt pricing, no context', cell_justify),
     Paragraph('Curated packs at better value, business context', cell_justify)],
    [Paragraph('Course Creators', cell_left), Paragraph('Udemy, Skillshare', cell_style),
     Paragraph('Comprehensive education', cell_justify), Paragraph('Time-consuming, expensive, theory-heavy', cell_justify),
     Paragraph('Immediate results, actionable templates', cell_justify)],
]
comp_table = Table(comp_data, colWidths=[1.2*inch, 0.9*inch, 1.3*inch, 1.5*inch, 1.4*inch])
comp_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    *[('BACKGROUND', (0, i), (-1, i), colors.white if i % 2 == 1 else TABLE_ODD) for i in range(1, 5)],
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))
story.append(Spacer(1, 18))
story.append(comp_table)
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 9.</b> Competitive Analysis Matrix', caption_style))
story.append(Spacer(1, 18))

# SECTION 10: IMPLEMENTATION ROADMAP
story.append(Paragraph('<b>10. Implementation Roadmap</b>', h1_style))
story.append(Spacer(1, 6))

story.append(Paragraph('<b>10.1 Phase 1: Foundation (Weeks 1-2)</b>', h2_style))
story.append(Paragraph(
    'The first two weeks focus exclusively on setting up the infrastructure for success. This includes finalizing '
    'the product content with accurate descriptions, setting up the Stripe account for payment processing, deploying '
    'the landing page with email capture functionality, and creating the lead magnet PDF. The goal is to have a '
    'fully functional conversion machine live and collecting emails before spending any time on marketing activities. '
    'Premature marketing is one of the most common mistakes new digital product businesses make, as it drives traffic '
    'to an unoptimized page that fails to convert.', body_style))

story.append(Paragraph('<b>10.2 Phase 2: Validation (Weeks 3-4)</b>', h2_style))
story.append(Paragraph(
    'With the landing page live, the next phase is about validating market demand. Drive targeted traffic to the '
    'page using free channels (Reddit, Pinterest, personal social media) and measure the conversion rate at each '
    'step: visitor-to-email-signup, email-to-product-view, and product-view-to-purchase. If the email signup rate '
    'is above 3%, the offer is resonating. If the purchase conversion rate is above 1%, the pricing is appropriate. '
    'If either metric falls significantly short, iterate on the page copy and product positioning before scaling. '
    'This validation phase should cost no more than $50-100 in total.', body_style))

story.append(Paragraph('<b>10.3 Phase 3: Growth (Months 2-3)</b>', h2_style))
story.append(Paragraph(
    'Once validation confirms market demand, the growth phase begins. This is where the content marketing engine '
    'kicks into high gear: publishing 2-3 blog posts per week targeting long-tail keywords, creating daily social '
    'media content, launching the email nurture sequence, and building a presence on Reddit and relevant online '
    'communities. The goal is to reach 1,000 monthly visitors and 300 email subscribers by the end of month three. '
    'Track everything using free analytics tools like Google Analytics and email platform metrics to identify which '
    'channels deliver the highest-quality traffic.', body_style))

story.append(Paragraph('<b>10.4 Phase 4: Scale (Months 4-6)</b>', h2_style))
story.append(Paragraph(
    'With proven conversion rates and a growing email list, it is time to introduce paid advertising and expand '
    'the product line. Start with small daily budgets ($5-10/day) on Meta (Facebook/Instagram) targeting freelancers '
    'and small business owners. Simultaneously, launch the first expansion pack and introduce the monthly subscription '
    'option for recurring prompt updates. The goal is to reach $2,000-$5,000 in monthly revenue by month six, with '
    'at least 20% of revenue coming from recurring subscriptions.', body_style))

story.append(Paragraph('<b>10.5 Phase 5: Optimize (Months 7-12)</b>', h2_style))
story.append(Paragraph(
    'The final phase focuses on optimization and diversification. Analyze which products sell best and create more '
    'products in the winning categories. Launch the community membership tier. A/B test landing page elements '
    'systematically. Develop strategic partnerships with complementary brands and influencers. Begin building an '
    'affiliate program where existing customers earn commissions for referring new buyers. By month twelve, the '
    'business should be generating $5,000-$15,000 in monthly revenue with a diversified revenue mix and a growing '
    'email list of 3,000-5,000 subscribers.', body_style))

# SECTION 11: RISK ASSESSMENT
story.append(Spacer(1, 12))
story.append(Paragraph('<b>11. Risk Assessment and Mitigation</b>', h1_style))
story.append(Spacer(1, 6))

risk_data = [
    [Paragraph('<b>Risk</b>', header_cell), Paragraph('<b>Likelihood</b>', header_cell),
     Paragraph('<b>Impact</b>', header_cell), Paragraph('<b>Mitigation Strategy</b>', header_cell)],
    [Paragraph('Low conversion rates', cell_left), Paragraph('Medium', cell_style),
     Paragraph('High', cell_style), Paragraph('A/B test page, iterate copy, add testimonials', cell_justify)],
    [Paragraph('Market saturation', cell_left), Paragraph('Medium', cell_style),
     Paragraph('Medium', cell_style), Paragraph('Niche focus, unique bundles, subscription value', cell_justify)],
    [Paragraph('Chargebacks/fraud', cell_left), Paragraph('Low', cell_style),
     Paragraph('Low', cell_style), Paragraph('Clear refund policy, Stripe protection, delivery confirmation', cell_justify)],
    [Paragraph('IP infringement claims', cell_left), Paragraph('Low', cell_style),
     Paragraph('Medium', cell_style), Paragraph('Original content creation, copyright notices, EULA', cell_justify)],
    [Paragraph('Tax compliance issues', cell_left), Paragraph('Medium', cell_style),
     Paragraph('Medium', cell_style), Paragraph('Track all income, set aside 25-30% for taxes, use Wave', cell_justify)],
    [Paragraph('Platform dependency', cell_left), Paragraph('Low', cell_style),
     Paragraph('High', cell_style), Paragraph('Own website, email list, diversify traffic sources', cell_justify)],
    [Paragraph('Burnout/solo founder risk', cell_left), Paragraph('High', cell_style),
     Paragraph('High', cell_style), Paragraph('Automate fulfillment, schedule content in batches, set boundaries', cell_justify)],
]
risk_table = Table(risk_data, colWidths=[1.4*inch, 0.9*inch, 0.8*inch, 3.2*inch])
risk_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    *[('BACKGROUND', (0, i), (-1, i), colors.white if i % 2 == 1 else TABLE_ODD) for i in range(1, 8)],
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))
story.append(Spacer(1, 18))
story.append(risk_table)
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 10.</b> Risk Assessment Matrix with Mitigation Strategies', caption_style))
story.append(Spacer(1, 18))

# SECTION 12: KPIs
story.append(Paragraph('<b>12. Key Performance Indicators</b>', h1_style))
story.append(Spacer(1, 6))
story.append(Paragraph(
    'Tracking the right metrics is essential for making data-driven decisions about where to invest time and money. '
    'The following KPIs should be monitored weekly during the first three months and monthly thereafter. Each metric '
    'has a target range that indicates healthy performance, and significant deviation from these ranges should trigger '
    'a review of the corresponding strategy or tactic.', body_style))

kpi_data = [
    [Paragraph('<b>KPI</b>', header_cell), Paragraph('<b>Target (Month 1-3)</b>', header_cell),
     Paragraph('<b>Target (Month 4-6)</b>', header_cell), Paragraph('<b>Target (Month 7-12)</b>', header_cell)],
    [Paragraph('Email Signup Rate', cell_left), Paragraph('3-5%', cell_style),
     Paragraph('5-8%', cell_style), Paragraph('8-12%', cell_style)],
    [Paragraph('Email-to-Purchase Rate', cell_left), Paragraph('1-2%', cell_style),
     Paragraph('2-4%', cell_style), Paragraph('3-5%', cell_style)],
    [Paragraph('Average Order Value', cell_left), Paragraph('$49-99', cell_style),
     Paragraph('$99-189', cell_style), Paragraph('$120-189', cell_style)],
    [Paragraph('Customer Acquisition Cost', cell_left), Paragraph('$0-5', cell_style),
     Paragraph('$5-15', cell_style), Paragraph('$5-20', cell_style)],
    [Paragraph('Monthly Recurring Revenue', cell_left), Paragraph('$0', cell_style),
     Paragraph('$100-500', cell_style), Paragraph('$500-2,000', cell_style)],
    [Paragraph('Email List Growth Rate', cell_left), Paragraph('10-20/week', cell_style),
     Paragraph('30-80/week', cell_style), Paragraph('100-300/week', cell_style)],
    [Paragraph('Churn Rate (subscriptions)', cell_left), Paragraph('N/A', cell_style),
     Paragraph('< 5%/month', cell_style), Paragraph('< 3%/month', cell_style)],
    [Paragraph('Net Promoter Score', cell_left), Paragraph('> 40', cell_style),
     Paragraph('> 50', cell_style), Paragraph('> 60', cell_style)],
]
kpi_table = Table(kpi_data, colWidths=[1.7*inch, 1.4*inch, 1.4*inch, 1.4*inch])
kpi_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    *[('BACKGROUND', (0, i), (-1, i), colors.white if i % 2 == 1 else TABLE_ODD) for i in range(1, 9)],
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))
story.append(Spacer(1, 18))
story.append(kpi_table)
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 11.</b> Key Performance Indicators by Growth Phase', caption_style))
story.append(Spacer(1, 18))

story.append(Paragraph(
    'By systematically tracking these metrics and making iterative improvements based on the data, FounderGrid can '
    'progress from a side hustle generating a few hundred dollars per month to a legitimate business generating '
    'five figures monthly within 12 months. The key is consistency in execution, willingness to iterate based on '
    'feedback, and patience during the early growth phase when results may seem slow.', body_style))

# Build
doc.build(story)
print(f"PDF built successfully: {pdf_path}")
