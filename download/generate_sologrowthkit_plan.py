#!/usr/bin/env python3
"""SoloGrowthKit Business Improvement Plan PDF Generator"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.platypus import (
    Paragraph, Spacer, PageBreak, Table, TableStyle,
    SimpleDocTemplate
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
import os

# ── Font Registration ──
pdfmetrics.registerFont(TTFont('Times New Roman', '/usr/share/fonts/truetype/english/Times-New-Roman.ttf'))
pdfmetrics.registerFont(TTFont('Calibri', '/usr/share/fonts/truetype/english/calibri-regular.ttf'))
registerFontFamily('Times New Roman', normal='Times New Roman', bold='Times New Roman')
registerFontFamily('Calibri', normal='Calibri', bold='Calibri')

# ── Colors ──
BRAND_GREEN = colors.HexColor('#059669')
BRAND_DARK = colors.HexColor('#0F172A')
TABLE_HEADER_COLOR = colors.HexColor('#1F4E79')
TABLE_HEADER_TEXT = colors.white
TABLE_ROW_EVEN = colors.white
TABLE_ROW_ODD = colors.HexColor('#F5F5F5')

# ── Styles ──
styles = getSampleStyleSheet()

cover_title = ParagraphStyle(
    name='CoverTitle', fontName='Times New Roman', fontSize=40,
    leading=48, alignment=TA_CENTER, spaceAfter=20, textColor=BRAND_GREEN
)
cover_subtitle = ParagraphStyle(
    name='CoverSubtitle', fontName='Times New Roman', fontSize=18,
    leading=26, alignment=TA_CENTER, spaceAfter=12, textColor=BRAND_DARK
)
cover_meta = ParagraphStyle(
    name='CoverMeta', fontName='Times New Roman', fontSize=13,
    leading=20, alignment=TA_CENTER, spaceAfter=8, textColor=colors.HexColor('#64748B')
)
h1_style = ParagraphStyle(
    name='H1', fontName='Times New Roman', fontSize=20,
    leading=26, spaceBefore=18, spaceAfter=10, textColor=BRAND_DARK
)
h2_style = ParagraphStyle(
    name='H2', fontName='Times New Roman', fontSize=15,
    leading=20, spaceBefore=14, spaceAfter=8, textColor=colors.HexColor('#1E293B')
)
body_style = ParagraphStyle(
    name='Body', fontName='Times New Roman', fontSize=10.5,
    leading=17, alignment=TA_JUSTIFY, spaceAfter=6
)
bullet_style = ParagraphStyle(
    name='Bullet', fontName='Times New Roman', fontSize=10.5,
    leading=17, alignment=TA_LEFT, spaceAfter=4, leftIndent=18, bulletIndent=6
)
caption_style = ParagraphStyle(
    name='Caption', fontName='Times New Roman', fontSize=9.5,
    leading=14, alignment=TA_CENTER, textColor=colors.HexColor('#475569'),
    spaceBefore=4, spaceAfter=6
)
header_cell = ParagraphStyle(
    name='HeaderCell', fontName='Times New Roman', fontSize=10,
    leading=14, alignment=TA_CENTER, textColor=colors.white
)
body_cell = ParagraphStyle(
    name='BodyCell', fontName='Times New Roman', fontSize=9.5,
    leading=13, alignment=TA_LEFT
)
body_cell_center = ParagraphStyle(
    name='BodyCellCenter', fontName='Times New Roman', fontSize=9.5,
    leading=13, alignment=TA_CENTER
)

# ── Helpers ──
def h1(text):
    return Paragraph(f'<b>{text}</b>', h1_style)

def h2(text):
    return Paragraph(f'<b>{text}</b>', h2_style)

def body(text):
    return Paragraph(text, body_style)

def bullet(text):
    return Paragraph(f'- {text}', bullet_style)

def make_table(headers, rows, col_widths=None):
    data = []
    header_row = [Paragraph(f'<b>{h}</b>', header_cell) for h in headers]
    data.append(header_row)
    for row in rows:
        data.append([Paragraph(str(c), body_cell) for c in row])
    t = Table(data, colWidths=col_widths)
    style_cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER_COLOR),
        ('TEXTCOLOR', (0, 0), (-1, 0), TABLE_HEADER_TEXT),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]
    for i in range(1, len(data)):
        bg = TABLE_ROW_EVEN if i % 2 == 1 else TABLE_ROW_ODD
        style_cmds.append(('BACKGROUND', (0, i), (-1, i), bg))
    t.setStyle(TableStyle(style_cmds))
    return t

# ── Build Document ──
output_path = '/home/z/my-project/download/SoloGrowthKit_Business_Plan.pdf'
doc = SimpleDocTemplate(
    output_path, pagesize=letter,
    leftMargin=0.9*inch, rightMargin=0.9*inch,
    topMargin=0.75*inch, bottomMargin=0.75*inch,
    title='SoloGrowthKit Business Plan',
    author='Z.ai', creator='Z.ai',
    subject='Comprehensive business improvement plan for SoloGrowthKit digital products'
)

story = []

# ══════════════ COVER PAGE ══════════════
story.append(Spacer(1, 140))
story.append(Paragraph('<b>SoloGrowthKit</b>', cover_title))
story.append(Spacer(1, 16))
story.append(Paragraph('Business Improvement Plan', cover_subtitle))
story.append(Spacer(1, 10))
story.append(Paragraph('The Growth Toolkit for Solo Founders', ParagraphStyle(
    name='CoverTagline', fontName='Times New Roman', fontSize=13,
    leading=18, alignment=TA_CENTER, textColor=BRAND_GREEN
)))
story.append(Spacer(1, 80))
story.append(Paragraph('Prepared: April 2026', cover_meta))
story.append(Paragraph('Confidential', cover_meta))
story.append(Paragraph('Version 1.0', cover_meta))
story.append(PageBreak())

# ══════════════ 1. EXECUTIVE SUMMARY ══════════════
story.append(h1('1. Executive Summary'))
story.append(body(
    'SoloGrowthKit is a digital products brand designed specifically for solo founders, freelancers, '
    'and solopreneurs who are building businesses on their own. The brand offers a curated collection '
    'of premium PDF toolkits that help solo operators save time, streamline operations, and accelerate '
    'growth without needing to hire a team or purchase expensive SaaS subscriptions. The core value '
    'proposition is simple: give solo founders the exact systems, prompts, and frameworks that successful '
    'businesses use, packaged in an affordable, instant-download format.'
))
story.append(body(
    'The business model centers on three flagship products: the AI Prompt Pack for Founders ($49), the '
    'Solo Ops Playbook ($79), and the Launch Marketing Kit ($99). Together, they form the All-Access Bundle '
    'priced at $189, representing a $38 savings over individual purchases. The target market encompasses over '
    '70 million freelancers and solopreneurs in the United States alone, with the global independent workforce '
    'exceeding 435 million people. This represents a massive addressable market with significant unmet demand '
    'for practical, affordable business tools.'
))
story.append(body(
    'This plan outlines a comprehensive strategy to validate the market, acquire customers through organic '
    'content marketing and social proof, build an email nurture sequence that converts leads into buyers, '
    'and scale revenue to between $15,000 and $50,000 within the first 12 months. The approach emphasizes '
    'lean operations, zero paid advertising during the initial phase, and a focus on building a sustainable '
    'brand that can expand into recurring revenue through subscription offerings and premium community access.'
))

# ══════════════ 2. MARKET ANALYSIS ══════════════
story.append(Spacer(1, 12))
story.append(h1('2. Market Analysis'))

story.append(h2('2.1 Target Market Size'))
story.append(body(
    'The market for digital products targeting independent workers has grown dramatically in recent years, '
    'driven by the rise of remote work, the creator economy, and a cultural shift toward entrepreneurship. '
    'According to Upwork research, the number of freelancers in the United States reached 70.4 million in '
    '2022, representing 36% of the total workforce. Globally, the independent workforce exceeds 435 million. '
    'These individuals are the primary audience for SoloGrowthKit products, as they consistently face the '
    'challenges of doing more with fewer resources, managing all aspects of their business alone, and '
    'competing against larger organizations with dedicated teams.'
))
story.append(Spacer(1, 18))

market_data = [
    ['US Freelancers', '70.4 million', '36% of workforce'],
    ['Global Independent Workers', '435+ million', 'Growing 3-5% annually'],
    ['US Solopreneurs', '51 million', 'Without employees'],
    ['Creator Economy', '50+ million', 'Content creators globally'],
    ['Digital Product Market', '$40B+ by 2028', 'CAGR of 12.5%'],
]
story.append(make_table(
    ['Metric', 'Value', 'Context'],
    market_data,
    col_widths=[2*inch, 1.6*inch, 2.6*inch]
))
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 1.</b> Target Market Overview', caption_style))

story.append(Spacer(1, 12))
story.append(h2('2.2 Customer Pain Points'))
story.append(body(
    'Through extensive analysis of freelancer communities, solopreneur forums, and independent worker surveys, '
    'five critical pain points emerge consistently. Solo founders spend excessive time on content creation, '
    'often investing 3 or more hours per piece of content that could be completed in 30 minutes with proper '
    'AI prompting and template systems. They lack operational structure, reinventing processes every week '
    'instead of building scalable systems. Marketing feels overwhelming because they do not know where to '
    'start or which channels actually deliver results for one-person businesses. They wear too many hats, '
    'leaving zero time for strategic thinking about growth. Finally, they cannot afford expensive tools or '
    'agency retainers, which typically cost $3,000 to $10,000 per month, forcing them to either go without '
    'professional resources or burn through their limited budgets.'
))

# ══════════════ 3. PRODUCT STRATEGY ══════════════
story.append(Spacer(1, 12))
story.append(h1('3. Product Strategy'))

story.append(h2('3.1 Product Lineup'))
story.append(body(
    'The SoloGrowthKit product lineup consists of three flagship digital products, each targeting a specific '
    'area of solo business operations. Every product is delivered as a professionally designed PDF that can be '
    'downloaded instantly and used on any device. The products are designed to be complementary, addressing '
    'the full lifecycle of solo business operations from content creation through operational systems to '
    'customer acquisition and marketing.'
))
story.append(Spacer(1, 18))

product_data = [
    ['AI Prompt Pack for Founders', '$49', '500+ proven AI prompts across 10 categories including content creation, marketing, business operations, sales, social media, email sequences, SEO, productivity, and customer service. Designed as a quick-reference tool that saves 10+ hours per week on routine tasks.'],
    ['Solo Ops Playbook', '$79', '20+ business templates including OKR frameworks, SWOT analysis, KPI dashboards, daily/weekly/monthly checklists, Standard Operating Procedures, and financial tracking templates. Provides the operational backbone that most solo founders lack.'],
    ['Launch Marketing Kit', '$99', 'Proven marketing strategy frameworks, ready-to-launch campaign templates, content calendar planners, ROI calculators with built-in formulas, and platform-specific social media guides. Eliminates the need for a $3,000/month marketing agency.'],
    ['All-Access Bundle', '$189', 'All three products at a $38 discount. This is the primary upsell target, offering the best value and highest margin for the business.'],
]
story.append(make_table(
    ['Product', 'Price', 'Description'],
    product_data,
    col_widths=[1.6*inch, 0.6*inch, 4*inch]
))
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 2.</b> SoloGrowthKit Product Lineup', caption_style))

story.append(Spacer(1, 12))
story.append(h2('3.2 Lead Magnet Strategy'))
story.append(body(
    'The primary customer acquisition mechanism is a free lead magnet titled "10 AI Prompts That Save Solo '
    'Founders 10+ Hours Per Week." This lead magnet serves multiple strategic purposes: it provides genuine '
    'value upfront to build trust, demonstrates the quality of the paid products, captures email addresses '
    'for the nurture sequence, and creates a natural upsell path to the full AI Prompt Pack. The lead magnet '
    'is prominently featured on the landing page in a dedicated section with a dark, high-contrast design '
    'that draws the eye and encourages immediate sign-up. The email capture form collects both name and email '
    'address, enabling personalized follow-up communications throughout the nurture sequence.'
))

# ══════════════ 4. REVENUE MODEL ══════════════
story.append(Spacer(1, 12))
story.append(h1('4. Revenue Model'))

story.append(h2('4.1 Pricing Strategy'))
story.append(body(
    'The pricing strategy follows a value-based model that positions each product as a fraction of the cost '
    'of hiring professional help. The AI Prompt Pack at $49 replaces approximately $200-$500 worth of '
    'prompt engineering courses. The Solo Ops Playbook at $79 replaces $1,000-$3,000 in business consulting '
    'fees. The Launch Marketing Kit at $99 replaces $3,000-$10,000 in monthly agency retainers. The '
    'All-Access Bundle at $189 provides maximum perceived value by offering all three products together at '
    'a significant discount, making it the easiest purchasing decision for serious buyers.'
))
story.append(Spacer(1, 18))

revenue_data = [
    ['AI Prompt Pack', '$49', '$1,225', '$4,900'],
    ['Solo Ops Playbook', '$79', '$1,975', '$7,900'],
    ['Launch Marketing Kit', '$99', '$2,475', '$9,900'],
    ['All-Access Bundle', '$189', '$5,670', '$22,680'],
    ['Blended Average', '$108', '$2,837', '$11,345'],
]
story.append(make_table(
    ['Product', 'Unit Price', 'Monthly (25 sales)', 'Monthly (100 sales)'],
    revenue_data,
    col_widths=[1.8*inch, 1.2*inch, 1.6*inch, 1.6*inch]
))
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 3.</b> Revenue Projections by Sales Volume', caption_style))

story.append(Spacer(1, 12))
story.append(h2('4.2 Financial Projections'))
story.append(body(
    'The financial model projects conservative, moderate, and optimistic scenarios over the first 12 months. '
    'The conservative scenario assumes slow organic growth with minimal marketing effort, reaching approximately '
    '$15,000 in total revenue by month 12. The moderate scenario projects steady growth through consistent '
    'content marketing and email nurturing, reaching approximately $30,000. The optimistic scenario accounts '
    'for potential viral content moments or strategic partnerships, projecting up to $50,000 in the first year.'
))
story.append(Spacer(1, 18))

projection_data = [
    ['Months 1-3', '$500-$1,500', '$1,000-$3,000', '$2,000-$5,000'],
    ['Months 4-6', '$2,000-$5,000', '$5,000-$10,000', '$8,000-$15,000'],
    ['Months 7-9', '$5,000-$8,000', '$10,000-$18,000', '$15,000-$25,000'],
    ['Months 10-12', '$7,000-$10,000', '$12,000-$20,000', '$18,000-$30,000'],
    ['Year 1 Total', '$15,000-$25,000', '$28,000-$51,000', '$43,000-$75,000'],
]
story.append(make_table(
    ['Period', 'Conservative', 'Moderate', 'Optimistic'],
    projection_data,
    col_widths=[1.4*inch, 1.6*inch, 1.6*inch, 1.6*inch]
))
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 4.</b> 12-Month Financial Projections', caption_style))

# ══════════════ 5. CUSTOMER ACQUISITION ══════════════
story.append(Spacer(1, 12))
story.append(h1('5. Customer Acquisition Strategy'))

story.append(h2('5.1 Organic Content Marketing'))
story.append(body(
    'The customer acquisition strategy prioritizes organic content marketing across multiple platforms to build '
    'sustainable, compounding traffic. Unlike paid advertising, which stops generating leads the moment spending '
    'ceases, organic content creates a permanent asset library that continues to drive traffic and conversions '
    'over time. The strategy focuses on four primary channels: Pinterest for visual discovery and passive '
    'content consumption, TikTok for short-form educational content that drives brand awareness, Reddit for '
    'authentic community engagement within solo founder subreddits, and Google SEO for long-term search visibility '
    'on high-intent keywords.'
))
story.append(Spacer(1, 18))

channel_data = [
    ['Pinterest', 'High', 'Low', 'Long-term', 'Infographics, carousel pins, blog pins linking to landing page. Pins have a 6-12 month shelf life, creating compounding traffic.'],
    ['TikTok', 'High', 'Very Low', 'Medium-term', 'Short-form educational videos showing AI prompts in action, quick business tips, and behind-the-scenes content.'],
    ['Reddit', 'Medium', 'Free', 'Long-term', 'Value-first participation in r/solopreneur, r/freelance, r/smallbusiness. No direct selling - build reputation first.'],
    ['Google SEO', 'Medium', 'Free', 'Long-term', 'Blog content targeting long-tail keywords like "AI prompts for solo founders" and "free marketing templates for freelancers".'],
    ['Twitter/X', 'Medium', 'Free', 'Short-term', 'Threads sharing quick tips, product updates, and engaging with the solopreneur community. Build in public.'],
    ['LinkedIn', 'Medium', 'Free', 'Medium-term', 'Long-form posts about solo business challenges. High conversion rate for professional audience.'],
]
story.append(make_table(
    ['Channel', 'Impact', 'Cost', 'Timeline', 'Strategy'],
    channel_data,
    col_widths=[0.9*inch, 0.7*inch, 0.7*inch, 0.9*inch, 3*inch]
))
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 5.</b> Customer Acquisition Channels', caption_style))

# ══════════════ 6. EMAIL NURTURE SEQUENCE ══════════════
story.append(Spacer(1, 12))
story.append(h1('6. Email Nurture Sequence'))

story.append(body(
    'The email nurture sequence is the primary conversion engine for SoloGrowthKit. When a visitor downloads '
    'the free lead magnet, they enter a carefully crafted 7-email sequence delivered over 14 days. Each email '
    'is designed to provide value, build trust, address objections, and create urgency for the paid products. '
    'The sequence follows a proven framework: deliver immediate value, share customer success stories, provide '
    'a sample of paid product quality, address common objections directly, create time-limited offers, and '
    'include clear calls-to-action at every stage.'
))
story.append(Spacer(1, 18))

email_data = [
    ['1', 'Day 0', 'Welcome + Free PDF Delivery', 'Deliver the lead magnet, set expectations, introduce SoloGrowthKit mission.'],
    ['2', 'Day 2', 'Quick Win: 3 More AI Prompts', 'Provide 3 additional high-value prompts not in the lead magnet. Build on the momentum.'],
    ['3', 'Day 4', 'The Solo Founder Struggle', 'Share a relatable story about solo business challenges. Introduce the paid products as the solution.'],
    ['4', 'Day 7', 'Customer Success Story', 'Feature a detailed testimonial with specific results. Include product screenshots and before/after metrics.'],
    ['5', 'Day 9', 'Free Sample: Inside the Playbook', 'Share one complete template from the Solo Ops Playbook. Let the quality sell itself.'],
    ['6', 'Day 12', 'Objection Handling FAQ', 'Address the top 5 objections: price, time to implement, industry fit, refund policy, and format.'],
    ['7', 'Day 14', 'Limited-Time Bundle Offer', 'Present the All-Access Bundle at the best price with a 48-hour deadline. Include strong social proof.'],
]
story.append(make_table(
    ['Email', 'Timing', 'Subject', 'Purpose'],
    email_data,
    col_widths=[0.5*inch, 0.7*inch, 1.8*inch, 3.2*inch]
))
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 6.</b> 7-Email Nurture Sequence (14 Days)', caption_style))

# ══════════════ 7. OPERATIONS & TECH STACK ══════════════
story.append(Spacer(1, 12))
story.append(h1('7. Operations and Technology'))

story.append(body(
    'SoloGrowthKit is designed to operate with minimal overhead and zero technical complexity for the founder. '
    'The entire technology stack leverages free or low-cost tools that require no server management, no database '
    'administration, and no DevOps expertise. The landing page is built with Next.js and deployed on Vercel free '
    'tier, which provides automatic SSL, global CDN, and zero-downtime deployments. Email collection uses a '
    'serverless API route with Prisma ORM and SQLite for data persistence. Payment processing will be handled '
    'through Stripe Checkout, with the secret key stored securely in environment variables that are never '
    'exposed in client-side code or shared with AI assistants.'
))
story.append(Spacer(1, 18))

tech_data = [
    ['Landing Page', 'Next.js + Tailwind CSS + shadcn/ui', 'Free (Vercel)'],
    ['Hosting', 'Vercel Free Tier', '$0/month'],
    ['Database', 'SQLite via Prisma ORM', '$0/month'],
    ['Email Collection', 'Custom API route', '$0/month'],
    ['Email Marketing', 'ConvertKit / MailerLite', '$0-$49/month'],
    ['Payment Processing', 'Stripe Checkout', '2.9% + 30c per transaction'],
    ['Analytics', 'Google Analytics + Vercel Analytics', '$0/month'],
    ['Domain', 'sologrowthkit.com (recommended)', '$10-$15/year'],
]
story.append(make_table(
    ['Function', 'Technology', 'Cost'],
    tech_data,
    col_widths=[1.6*inch, 2.6*inch, 2*inch]
))
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 7.</b> Technology Stack and Costs', caption_style))

# ══════════════ 8. LEGAL & COMPLIANCE ══════════════
story.append(Spacer(1, 12))
story.append(h1('8. Legal and Compliance'))

story.append(body(
    'Operating a digital products business requires attention to several legal and compliance requirements. '
    'While SoloGrowthKit is structured as a sole proprietorship initially, which minimizes administrative '
    'burden, there are still critical legal foundations that must be established before accepting payments. '
    'These include clear terms of service, a privacy policy compliant with data protection regulations, a '
    'refund policy that builds customer trust, proper copyright notices on all digital products, and income '
    'tax reporting obligations. As revenue grows beyond $10,000 annually, it may be worth considering forming '
    'an LLC for personal liability protection, though this is not required at launch.'
))
story.append(Spacer(1, 18))

legal_data = [
    ['Terms of Service', 'Before launch', 'Defines purchase terms, product usage rights, and dispute resolution.'],
    ['Privacy Policy', 'Before launch', 'Compliant with GDPR, CCPA. Details data collection, storage, and subscriber rights.'],
    ['Refund Policy', 'Before launch', '30-day money-back guarantee. Builds trust and reduces purchase anxiety.'],
    ['Copyright Notices', 'Before launch', 'All PDFs include copyright marks. Products are for personal/business use only.'],
    ['Business Registration', 'Within 30 days', 'Register as sole proprietorship with state/local authorities. Obtain EIN from IRS.'],
    ['Income Tax Reporting', 'Quarterly', 'Report digital product income on Schedule C. Set aside 25-30% for taxes.'],
    ['LLC Formation (Optional)', 'After $10K revenue', 'Provides personal liability protection. Costs $100-$500 depending on state.'],
]
story.append(make_table(
    ['Requirement', 'Timeline', 'Details'],
    legal_data,
    col_widths=[1.5*inch, 1.2*inch, 3.5*inch]
))
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 8.</b> Legal Compliance Roadmap', caption_style))

# ══════════════ 9. IMPLEMENTATION PHASES ══════════════
story.append(Spacer(1, 12))
story.append(h1('9. Implementation Timeline'))

story.append(body(
    'The implementation follows a four-phase approach that prioritizes speed to market and continuous iteration. '
    'Phase 1 focuses on launching the minimum viable product: the landing page with email capture and the first '
    'product. Phase 2 expands the product line and begins content marketing. Phase 3 introduces the email nurture '
    'sequence and Stripe integration for payments. Phase 4 optimizes conversion rates and explores expansion '
    'opportunities such as subscription models and community features. Each phase builds on the previous one, '
    'ensuring that the business grows sustainably without overextending resources or taking on unnecessary risk.'
))
story.append(Spacer(1, 18))

phase_data = [
    ['Phase 1: Launch', 'Weeks 1-2', 'Deploy landing page on Vercel. Set up email capture. Create first product PDF. Begin collecting leads.'],
    ['Phase 2: Expand', 'Weeks 3-4', 'Complete all three products. Launch content on Pinterest and TikTok. Begin blog SEO strategy.'],
    ['Phase 3: Convert', 'Weeks 5-8', 'Build email nurture sequence. Integrate Stripe payments. Launch paid products. Start Reddit marketing.'],
    ['Phase 4: Optimize', 'Weeks 9-12', 'A/B test landing page elements. Optimize email sequences based on open/click rates. Explore subscription model.'],
    ['Phase 5: Scale', 'Months 4-6', 'Expand to LinkedIn and Twitter. Create expansion packs. Build community (Discord/Circle).'],
    ['Phase 6: Sustain', 'Months 7-12', 'Launch subscription tier. Add affiliate program. Explore partnerships. Consider LLC formation.'],
]
story.append(make_table(
    ['Phase', 'Timeline', 'Key Actions'],
    phase_data,
    col_widths=[1.3*inch, 1.2*inch, 3.7*inch]
))
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 9.</b> Implementation Timeline', caption_style))

# ══════════════ 10. RISK ASSESSMENT ══════════════
story.append(Spacer(1, 12))
story.append(h1('10. Risk Assessment'))

story.append(body(
    'Every business venture carries inherent risks, and SoloGrowthKit is no exception. The following risk '
    'assessment identifies the most significant threats to the business, evaluates their likelihood and '
    'potential impact, and outlines specific mitigation strategies for each. The overall risk profile is '
    'favorable because the business requires minimal upfront investment, has no recurring costs beyond '
    'optional email marketing tools, and can pivot quickly based on market feedback. The primary risks '
    'relate to market validation, competition, and content creation sustainability.'
))
story.append(Spacer(1, 18))

risk_data = [
    ['Low demand / no one buys', 'Medium', 'High', 'Validate with lead magnet first. Collect 500+ emails before launching paid products.'],
    ['Market saturation', 'Low', 'Medium', 'Niche down to solo founders specifically. Focus on unique frameworks, not generic templates.'],
    ['Content creation burnout', 'Medium', 'Medium', 'Batch create content. Repurpose across platforms. Use AI to assist (not replace) creation.'],
    ['Product quality complaints', 'Low', 'High', 'Beta test with 10-20 early users. Offer 30-day guarantee. Iterate based on feedback.'],
    ['Platform dependency', 'Low', 'Low', 'Own the email list. Build landing page with portable tech (Next.js). Can migrate from Vercel.'],
    ['Copycat competitors', 'Medium', 'Low', 'Build strong brand identity. Focus on customer relationships. Continuous product improvement.'],
]
story.append(make_table(
    ['Risk', 'Likelihood', 'Impact', 'Mitigation'],
    risk_data,
    col_widths=[1.5*inch, 0.8*inch, 0.7*inch, 3.2*inch]
))
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 10.</b> Risk Assessment Matrix', caption_style))

# ══════════════ 11. KPIs ══════════════
story.append(Spacer(1, 12))
story.append(h1('11. Key Performance Indicators'))

story.append(body(
    'Tracking the right metrics is essential for making data-driven decisions and identifying areas for '
    'improvement. SoloGrowthKit will monitor a focused set of key performance indicators across four '
    'categories: acquisition metrics that measure how effectively the business attracts visitors and '
    'captures leads, conversion metrics that track the efficiency of the sales funnel, revenue metrics '
    'that evaluate business financial health, and engagement metrics that assess customer satisfaction '
    'and long-term value. Each KPI has a specific benchmark target based on industry averages for digital '
    'product businesses, and will be reviewed weekly during the first 90 days and monthly thereafter.'
))
story.append(Spacer(1, 18))

kpi_data = [
    ['Landing Page Visitors', 'Acquisition', '1,000/month (Month 3)', 'Google Analytics'],
    ['Email Capture Rate', 'Acquisition', '5-10% of visitors', 'Vercel + DB Analytics'],
    ['Lead Magnet Downloads', 'Acquisition', '50-100/month (Month 3)', 'Email Platform'],
    ['Email Open Rate', 'Engagement', '35-50%', 'Email Platform'],
    ['Email Click Rate', 'Engagement', '3-7%', 'Email Platform'],
    ['Lead-to-Customer Rate', 'Conversion', '2-5%', 'Stripe + Email Platform'],
    ['Average Order Value', 'Revenue', '$108-$189', 'Stripe Dashboard'],
    ['Monthly Revenue', 'Revenue', '$2,837+ (Month 6)', 'Stripe Dashboard'],
    ['Refund Rate', 'Revenue', 'Under 5%', 'Stripe Dashboard'],
    ['Net Promoter Score', 'Engagement', '40+', 'Post-purchase Survey'],
]
story.append(make_table(
    ['KPI', 'Category', 'Target', 'Tracking Tool'],
    kpi_data,
    col_widths=[1.5*inch, 0.9*inch, 1.8*inch, 1.6*inch]
))
story.append(Spacer(1, 6))
story.append(Paragraph('<b>Table 11.</b> Key Performance Indicators and Targets', caption_style))

# ══════════════ 12. FUTURE GROWTH ══════════════
story.append(Spacer(1, 12))
story.append(h1('12. Future Growth Opportunities'))

story.append(h2('12.1 Subscription Model'))
story.append(body(
    'The most significant revenue expansion opportunity is transitioning from one-time sales to a recurring '
    'subscription model. A "SoloGrowthKit Pro" membership at $19-$29/month would provide ongoing access to '
    'new templates, updated AI prompts, monthly strategy guides, and a private community of fellow solo '
    'founders. Subscription revenue provides predictable monthly income, increases customer lifetime value '
    'from an average of $108-$189 to potentially $228-$348 per year, and creates a competitive moat through '
    'community lock-in. The subscription tier should be introduced after the initial product suite has proven '
    'demand and after building an email list of at least 1,000 subscribers.'
))

story.append(h2('12.2 Expansion Products'))
story.append(body(
    'Once the core brand is established and the customer base is actively engaged, SoloGrowthKit can expand '
    'into adjacent product categories. Potential expansion products include industry-specific prompt packs '
    'tailored for niches like freelance designers, consultants, coaches, and e-commerce operators. A "Solo '
    'Finance Tracker" product that includes bookkeeping templates, tax planning guides, and profit tracking '
    'spreadsheets addresses a critical pain point for solo founders. Video course versions of the existing '
    'PDFs could command premium pricing of $149-$299 per course. An affiliate program would incentivize '
    'existing customers to promote SoloGrowthKit to their networks, creating a scalable acquisition channel '
    'that only pays for results.'
))

story.append(h2('12.3 Community and Platform'))
story.append(body(
    'Building a private community around SoloGrowthKit represents the highest long-term value opportunity. '
    'A community platform hosted on Circle or Discord would provide monthly live Q&A sessions with the founder, '
    'peer networking and accountability groups, collaborative templates and crowdsourced prompt libraries, '
    'exclusive early access to new products, and co-working sessions and virtual meetups. Community membership '
    'could be positioned as a premium add-on at $9-$15/month or bundled with the Pro subscription. The '
    'community creates a powerful retention mechanism because members receive ongoing value beyond the initial '
    'product purchase, significantly reducing churn and increasing word-of-mouth referrals.'
))

# ── Build ──
doc.build(story)
print(f"PDF generated: {output_path}")
