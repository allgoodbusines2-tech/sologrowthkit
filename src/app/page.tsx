'use client'

import { useState, useRef, FormEvent } from 'react'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardFooter, CardHeader, CardTitle, CardDescription } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from '@/components/ui/accordion'
import { Badge } from '@/components/ui/badge'
import { Separator } from '@/components/ui/separator'
import {
  Lightbulb,
  ClipboardList,
  Rocket,
  Clock,
  RefreshCcw,
  Megaphone,
  Users,
  Download,
  Settings,
  TrendingUp,
  Quote,
  Mail,
  CheckCircle2,
  Package,
  Menu,
  X,
  ArrowRight,
  Star,
  Sparkles,
  FileText,
  Zap,
  Shield,
  ChevronDown,
} from 'lucide-react'

/* ─── Data ─── */

const products = [
  {
    icon: Lightbulb,
    name: 'AI Prompt Pack for Founders',
    price: 49,
    description: '500+ ready-to-use AI prompts across 10 categories',
    features: [
      '500+ proven prompts across 10 categories',
      'Content creation, marketing & business ops',
      'Sales, social media & email sequences',
      'SEO, productivity & customer service',
      'Professional PDF, instant download',
    ],
  },
  {
    icon: ClipboardList,
    name: 'Solo Ops Playbook',
    price: 79,
    description: '20+ business templates, SOPs & financial trackers',
    features: [
      '20+ business templates (OKR, SWOT, KPI)',
      'Daily, weekly & monthly checklists',
      'Standard Operating Procedures (SOPs)',
      'Financial tracking templates',
      'Professional PDF, instant download',
    ],
  },
  {
    icon: Rocket,
    name: 'Launch Marketing Kit',
    price: 99,
    description: 'Proven marketing strategy frameworks & campaign templates',
    features: [
      'Proven marketing strategy frameworks',
      'Ready-to-launch campaign templates',
      'Content calendar planners',
      'ROI calculators with built-in formulas',
      'Platform-specific social media guides',
    ],
  },
]

const painPoints = [
  {
    icon: Clock,
    title: 'Spending 3+ hours writing content',
    description: 'That should take 30 minutes — if you had the right prompts and templates.',
  },
  {
    icon: RefreshCcw,
    title: 'No systems in place',
    description: "Reinventing the wheel every week instead of building scalable processes.",
  },
  {
    icon: Megaphone,
    title: 'Marketing feels overwhelming',
    description: "Don't know where to start or what actually works for solo founders.",
  },
  {
    icon: Users,
    title: 'Wearing too many hats',
    description: 'With zero time to breathe, let alone think strategically about growth.',
  },
]

const steps = [
  {
    icon: Download,
    title: 'Download',
    description: 'Get instant access to your products right after purchase. PDFs work on any device.',
  },
  {
    icon: Settings,
    title: 'Customize',
    description: 'Make templates your own in minutes. Fill in your details and start using them immediately.',
  },
  {
    icon: TrendingUp,
    title: 'Grow',
    description: 'Save time, look professional, and scale faster with proven systems.',
  },
]

const testimonials = [
  {
    quote:
      "These prompts cut my content creation time by 70%. I went from spending 4 hours on blog posts to under an hour.",
    name: 'Sarah K.',
    role: 'Freelance Writer',
    rating: 5,
  },
  {
    quote:
      'The ops playbook gave my business structure I desperately needed. Now I actually have systems.',
    name: 'Marcus T.',
    role: 'Consultant',
    rating: 5,
  },
  {
    quote:
      'Worth every penny. The marketing kit alone saved me from hiring a $3,000/month agency.',
    name: 'Jessica L.',
    role: 'E-commerce Owner',
    rating: 5,
  },
]

const faqs = [
  {
    question: 'What format are the products in?',
    answer:
      'All products are professional PDFs you can download instantly and use on any device. They work perfectly on desktop, tablet, and mobile.',
  },
  {
    question: 'Can I use these for my specific industry?',
    answer:
      'Yes! Our prompts and templates are designed to be customizable for any business type. Whether you are in consulting, e-commerce, SaaS, or creative services — everything adapts to your needs.',
  },
  {
    question: 'Is this a subscription?',
    answer:
      'No, it\'s a one-time purchase. You get lifetime access to all purchased products. No recurring fees, no hidden charges.',
  },
  {
    question: 'Do you offer refunds?',
    answer:
      'Yes, we offer a 30-day money-back guarantee. If you\'re not satisfied for any reason, email us and we\'ll refund you in full — no questions asked.',
  },
  {
    question: 'How do I access my products after purchase?',
    answer:
      'After payment, you\'ll receive an instant download link via email. You can also download directly from the purchase confirmation page. Access never expires.',
  },
  {
    question: 'Can I buy just one product?',
    answer:
      'Absolutely. Each product is available individually, or you can save $38 with the All-Access Bundle. Mix and match based on what your business needs most.',
  },
]

/* ─── Component ─── */

export default function Home() {
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle')
  const [errorMessage, setErrorMessage] = useState('')
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)
  const formRef = useRef<HTMLDivElement>(null)

  const scrollTo = (id: string) => {
    setMobileMenuOpen(false)
    document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' })
  }

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault()
    setStatus('loading')
    setErrorMessage('')

    try {
      const res = await fetch('/api/subscribe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: name.trim(), email: email.trim() }),
      })

      const data = await res.json()

      if (res.ok) {
        setStatus('success')
        setName('')
        setEmail('')
      } else {
        setStatus('error')
        setErrorMessage(data.error || 'Something went wrong. Please try again.')
      }
    } catch {
      setStatus('error')
      setErrorMessage('Network error. Please check your connection and try again.')
    }
  }

  return (
    <div className="min-h-screen bg-white">
      {/* ═══════ NAVIGATION ═══════ */}
      <nav className="fixed top-0 left-0 right-0 z-50 bg-white/80 backdrop-blur-lg border-b border-slate-100">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            {/* Logo */}
            <button
              onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
              className="flex items-center gap-2"
            >
              <Package className="h-6 w-6 text-emerald-600" />
              <span className="text-lg font-bold text-slate-900">
                Solo<span className="text-emerald-600">GrowthKit</span>
              </span>
            </button>

            {/* Desktop Nav */}
            <div className="hidden md:flex items-center gap-8">
              <button
                onClick={() => scrollTo('products')}
                className="text-sm font-medium text-slate-600 hover:text-emerald-600 transition-colors"
              >
                Products
              </button>
              <button
                onClick={() => scrollTo('pricing')}
                className="text-sm font-medium text-slate-600 hover:text-emerald-600 transition-colors"
              >
                Pricing
              </button>
              <button
                onClick={() => scrollTo('faq')}
                className="text-sm font-medium text-slate-600 hover:text-emerald-600 transition-colors"
              >
                FAQ
              </button>
              <Button
                onClick={() => scrollTo('lead-magnet')}
                className="bg-emerald-600 hover:bg-emerald-700 text-white"
              >
                Get Free Guide
              </Button>
            </div>

            {/* Mobile Menu Button */}
            <button
              className="md:hidden p-2 text-slate-600 hover:text-slate-900"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            >
              {mobileMenuOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
            </button>
          </div>
        </div>

        {/* Mobile Menu */}
        {mobileMenuOpen && (
          <div className="md:hidden bg-white border-t border-slate-100 px-4 py-4 space-y-3">
            <button
              onClick={() => scrollTo('products')}
              className="block w-full text-left text-sm font-medium text-slate-600 hover:text-emerald-600 py-2"
            >
              Products
            </button>
            <button
              onClick={() => scrollTo('pricing')}
              className="block w-full text-left text-sm font-medium text-slate-600 hover:text-emerald-600 py-2"
            >
              Pricing
            </button>
            <button
              onClick={() => scrollTo('faq')}
              className="block w-full text-left text-sm font-medium text-slate-600 hover:text-emerald-600 py-2"
            >
              FAQ
            </button>
            <Button
              onClick={() => scrollTo('lead-magnet')}
              className="w-full bg-emerald-600 hover:bg-emerald-700 text-white"
            >
              Get Free Guide
            </Button>
          </div>
        )}
      </nav>

      {/* ═══════ HERO SECTION ═══════ */}
      <section className="relative pt-32 pb-20 md:pt-40 md:pb-28 overflow-hidden">
        {/* Background Pattern */}
        <div className="absolute inset-0 bg-gradient-to-br from-emerald-50 via-white to-teal-50" />
        <div className="absolute inset-0 opacity-[0.03]" style={{
          backgroundImage: `url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23059669' fill-opacity='1'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")`,
        }} />

        <div className="relative max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <Badge className="mb-6 bg-emerald-100 text-emerald-700 border-emerald-200 px-3 py-1 text-sm font-medium inline-flex items-center gap-1.5">
            <Sparkles className="h-3.5 w-3.5" />
            Built for Solo Founders
          </Badge>

          <h1 className="text-4xl sm:text-5xl md:text-6xl font-extrabold text-slate-900 tracking-tight leading-tight max-w-4xl mx-auto">
            Stop Wasting Hours on Tasks{' '}
            <span className="text-emerald-600">AI Can Do in Seconds</span>
          </h1>

          <p className="mt-6 text-lg sm:text-xl text-slate-600 max-w-2xl mx-auto leading-relaxed">
            500+ proven AI prompts, ready-to-use business templates, and marketing playbooks
            built specifically for solo founders who need to do more with less.
          </p>

          <div className="mt-10 flex flex-col sm:flex-row items-center justify-center gap-4">
            <Button
              onClick={() => scrollTo('lead-magnet')}
              size="lg"
              className="bg-emerald-600 hover:bg-emerald-700 text-white px-8 py-3 text-base font-semibold rounded-lg shadow-lg shadow-emerald-600/20"
            >
              Download Free Guide
              <ArrowRight className="ml-1 h-4 w-4" />
            </Button>
            <Button
              onClick={() => scrollTo('products')}
              variant="outline"
              size="lg"
              className="border-emerald-600 text-emerald-700 hover:bg-emerald-50 px-8 py-3 text-base font-semibold rounded-lg"
            >
              View Products
            </Button>
          </div>

          <div className="mt-8 flex items-center justify-center gap-2 text-sm text-slate-500">
            <CheckCircle2 className="h-4 w-4 text-emerald-500" />
            <span>Join <strong className="text-slate-700">500+</strong> solo founders already saving 10+ hours per week</span>
          </div>
        </div>
      </section>

      {/* ═══════ PAIN POINTS ═══════ */}
      <section className="py-20 md:py-24 bg-white">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-14">
            <h2 className="text-3xl sm:text-4xl font-bold text-slate-900">Sound Familiar?</h2>
            <p className="mt-3 text-slate-600 text-lg max-w-2xl mx-auto">
              If any of these sound like you, you&apos;re in the right place.
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {painPoints.map((point, index) => (
              <Card
                key={index}
                className="border-slate-200 hover:border-emerald-200 hover:shadow-md transition-all duration-300 bg-white"
              >
                <CardContent className="pt-6 flex flex-col items-center text-center">
                  <div className="h-12 w-12 rounded-full bg-red-50 flex items-center justify-center mb-4">
                    <point.icon className="h-6 w-6 text-red-500" />
                  </div>
                  <h3 className="font-semibold text-slate-900 mb-2">{point.title}</h3>
                  <p className="text-sm text-slate-600 leading-relaxed">{point.description}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* ═══════ PRODUCTS ═══════ */}
      <section id="products" className="py-20 md:py-24 bg-slate-50">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-14">
            <h2 className="text-3xl sm:text-4xl font-bold text-slate-900">
              Everything You Need to Run Your Business Like a Pro
            </h2>
            <p className="mt-3 text-slate-600 text-lg max-w-2xl mx-auto">
              Professional tools designed to save you hours every week.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {products.map((product, index) => (
              <Card
                key={index}
                className="border-slate-200 hover:shadow-lg transition-all duration-300 bg-white flex flex-col"
              >
                <CardHeader className="pb-0">
                  <div className="h-14 w-14 rounded-xl bg-emerald-50 flex items-center justify-center mb-4">
                    <product.icon className="h-7 w-7 text-emerald-600" />
                  </div>
                  <CardTitle className="text-xl text-slate-900">{product.name}</CardTitle>
                  <CardDescription className="text-slate-600">{product.description}</CardDescription>
                </CardHeader>
                <CardContent className="flex-1">
                  <div className="flex items-baseline gap-1 mb-4">
                    <span className="text-3xl font-bold text-slate-900">${product.price}</span>
                    <span className="text-sm text-slate-500">one-time</span>
                  </div>
                  <Separator className="mb-4" />
                  <ul className="space-y-3">
                    {product.features.map((feature, fIdx) => (
                      <li key={fIdx} className="flex items-start gap-2.5 text-sm text-slate-600">
                        <CheckCircle2 className="h-4 w-4 text-emerald-500 mt-0.5 shrink-0" />
                        <span>{feature}</span>
                      </li>
                    ))}
                  </ul>
                </CardContent>
                <CardFooter className="pt-0">
                  <Button
                    onClick={() => scrollTo('final-cta')}
                    variant="outline"
                    className="w-full border-emerald-600 text-emerald-700 hover:bg-emerald-50 font-semibold"
                  >
                    Learn More
                    <ArrowRight className="ml-1 h-4 w-4" />
                  </Button>
                </CardFooter>
              </Card>
            ))}
          </div>

          {/* Bundle Deal */}
          <div id="pricing" className="mt-12">
            <Card className="bg-gradient-to-r from-emerald-600 to-teal-600 border-0 text-white shadow-xl shadow-emerald-600/20">
              <CardContent className="py-8 px-6 md:px-12 flex flex-col md:flex-row items-center justify-between gap-6">
                <div className="text-center md:text-left">
                  <Badge className="bg-white/20 text-white border-white/30 mb-3 text-sm">
                    <Zap className="h-3 w-3 mr-1" />
                    Best Value — Save $38
                  </Badge>
                  <h3 className="text-2xl font-bold">All-Access Bundle</h3>
                  <p className="text-emerald-100 mt-1">
                    Get all 3 products: AI Prompt Pack, Solo Ops Playbook &amp; Launch Marketing Kit
                  </p>
                </div>
                <div className="flex items-center gap-4 shrink-0">
                  <div className="text-center">
                    <div className="text-sm text-emerald-200 line-through">$227</div>
                    <div className="text-4xl font-bold">$189</div>
                    <div className="text-sm text-emerald-200">One-time payment</div>
                  </div>
                  <Button
                    onClick={() => scrollTo('final-cta')}
                    size="lg"
                    className="bg-white text-emerald-700 hover:bg-emerald-50 font-bold px-8 py-3 rounded-lg shadow-lg"
                  >
                    Get the Bundle
                    <ArrowRight className="ml-1 h-4 w-4" />
                  </Button>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* ═══════ LEAD MAGNET ═══════ */}
      <section
        id="lead-magnet"
        ref={formRef}
        className="py-20 md:py-24 bg-gradient-to-b from-slate-900 to-slate-800 text-white relative overflow-hidden"
      >
        {/* Subtle pattern */}
        <div className="absolute inset-0 opacity-5" style={{
          backgroundImage: `url("data:image/svg+xml,%3Csvg width='40' height='40' viewBox='0 0 40 40' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%23ffffff' fill-opacity='1' fill-rule='evenodd'%3E%3Cpath d='M0 40L40 0H20L0 20M40 40V20L20 40'/%3E%3C/g%3E%3C/svg%3E")`,
        }} />

        <div className="relative max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="inline-flex items-center gap-2 bg-emerald-500/20 border border-emerald-500/30 rounded-full px-4 py-1.5 mb-6">
            <FileText className="h-4 w-4 text-emerald-400" />
            <span className="text-sm font-medium text-emerald-300">Free PDF Download</span>
          </div>

          <h2 className="text-3xl sm:text-4xl font-bold leading-tight">
            Free: 10 AI Prompts That Save Solo Founders{' '}
            <span className="text-emerald-400">10+ Hours Per Week</span>
          </h2>

          <p className="mt-4 text-lg text-slate-300 max-w-xl mx-auto leading-relaxed">
            Get our most popular prompts — the ones solo founders use every single day to write
            content, plan marketing, and run operations faster.
          </p>

          {status === 'success' ? (
            <div className="mt-10 bg-emerald-500/20 border border-emerald-500/30 rounded-xl p-8 inline-flex flex-col items-center gap-3">
              <CheckCircle2 className="h-12 w-12 text-emerald-400" />
              <p className="text-xl font-semibold text-emerald-300">You&apos;re in!</p>
              <p className="text-slate-300">
                Check your inbox for the free guide. It should arrive within a few minutes.
              </p>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="mt-10 max-w-md mx-auto">
              <div className="flex flex-col gap-3">
                <Input
                  type="text"
                  placeholder="Your name"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  className="h-12 bg-white/10 border-white/20 text-white placeholder:text-slate-400 focus-visible:border-emerald-500 focus-visible:ring-emerald-500/50 rounded-lg"
                  required
                />
                <Input
                  type="email"
                  placeholder="you@example.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="h-12 bg-white/10 border-white/20 text-white placeholder:text-slate-400 focus-visible:border-emerald-500 focus-visible:ring-emerald-500/50 rounded-lg"
                  required
                />
                <Button
                  type="submit"
                  disabled={status === 'loading'}
                  size="lg"
                  className="h-12 bg-emerald-600 hover:bg-emerald-700 text-white font-semibold rounded-lg shadow-lg shadow-emerald-600/30 mt-2"
                >
                  {status === 'loading' ? (
                    <span className="flex items-center gap-2">
                      <span className="h-4 w-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                      Subscribing...
                    </span>
                  ) : (
                    <span className="flex items-center gap-2">
                      <Mail className="h-4 w-4" />
                      Download Free Guide
                    </span>
                  )}
                </Button>
              </div>
              {status === 'error' && errorMessage && (
                <p className="mt-3 text-sm text-red-400">{errorMessage}</p>
              )}
              <p className="mt-4 text-xs text-slate-400">
                No spam. Unsubscribe anytime. We respect your inbox.
              </p>
            </form>
          )}
        </div>
      </section>

      {/* ═══════ HOW IT WORKS ═══════ */}
      <section className="py-20 md:py-24 bg-white">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-14">
            <h2 className="text-3xl sm:text-4xl font-bold text-slate-900">How It Works</h2>
            <p className="mt-3 text-slate-600 text-lg max-w-2xl mx-auto">
              From download to results in three simple steps.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 relative">
            {/* Connector lines (desktop only) */}
            <div className="hidden md:block absolute top-16 left-1/3 right-1/3 h-0.5 bg-gradient-to-r from-emerald-200 via-emerald-300 to-emerald-200" />

            {steps.map((step, index) => (
              <div key={index} className="flex flex-col items-center text-center relative">
                <div className="h-16 w-16 rounded-full bg-emerald-600 flex items-center justify-center mb-6 relative z-10 shadow-lg shadow-emerald-600/20">
                  <step.icon className="h-7 w-7 text-white" />
                </div>
                <Badge variant="outline" className="border-emerald-200 text-emerald-700 mb-3">
                  Step {index + 1}
                </Badge>
                <h3 className="text-xl font-bold text-slate-900 mb-2">{step.title}</h3>
                <p className="text-slate-600 leading-relaxed max-w-xs">{step.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ═══════ TESTIMONIALS ═══════ */}
      <section className="py-20 md:py-24 bg-slate-50">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-14">
            <h2 className="text-3xl sm:text-4xl font-bold text-slate-900">
              Loved by Solo Founders
            </h2>
            <p className="mt-3 text-slate-600 text-lg max-w-2xl mx-auto">
              Here&apos;s what early customers are saying about our products.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {testimonials.map((testimonial, index) => (
              <Card key={index} className="border-slate-200 bg-white hover:shadow-md transition-shadow">
                <CardContent className="pt-6">
                  <div className="flex gap-1 mb-4">
                    {Array.from({ length: testimonial.rating }).map((_, i) => (
                      <Star key={i} className="h-4 w-4 fill-yellow-400 text-yellow-400" />
                    ))}
                  </div>
                  <Quote className="h-6 w-6 text-slate-200 mb-3" />
                  <p className="text-slate-700 leading-relaxed italic mb-6">
                    &ldquo;{testimonial.quote}&rdquo;
                  </p>
                  <Separator className="mb-4" />
                  <div>
                    <p className="font-semibold text-slate-900">{testimonial.name}</p>
                    <p className="text-sm text-slate-500">{testimonial.role}</p>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* ═══════ FAQ ═══════ */}
      <section id="faq" className="py-20 md:py-24 bg-white">
        <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-14">
            <h2 className="text-3xl sm:text-4xl font-bold text-slate-900">
              Frequently Asked Questions
            </h2>
            <p className="mt-3 text-slate-600 text-lg">
              Everything you need to know about our products.
            </p>
          </div>

          <Accordion type="single" collapsible className="w-full">
            {faqs.map((faq, index) => (
              <AccordionItem key={index} value={`item-${index}`} className="border-slate-200">
                <AccordionTrigger className="text-left text-slate-900 font-medium hover:text-emerald-600 hover:no-underline">
                  {faq.question}
                </AccordionTrigger>
                <AccordionContent className="text-slate-600 leading-relaxed">
                  {faq.answer}
                </AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        </div>
      </section>

      {/* ═══════ FINAL CTA ═══════ */}
      <section id="final-cta" className="py-20 md:py-24 bg-gradient-to-br from-emerald-600 to-teal-700 text-white relative overflow-hidden">
        <div className="absolute inset-0 opacity-10" style={{
          backgroundImage: `url("data:image/svg+xml,%3Csvg width='80' height='80' viewBox='0 0 80 80' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='1'%3E%3Cpath d='M50 50c0-5.523 4.477-10 10-10s10 4.477 10 10-4.477 10-10 10c0 5.523-4.477 10-10 10s-10-4.477-10-10 4.477-10 10-10zM10 10c0-5.523 4.477-10 10-10s10 4.477 10 10-4.477 10-10 10c0 5.523-4.477 10-10 10S0 25.523 0 20s4.477-10 10-10z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")`,
        }} />

        <div className="relative max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <Shield className="h-12 w-12 text-emerald-300 mx-auto mb-6 opacity-60" />
          <h2 className="text-3xl sm:text-4xl font-bold leading-tight">
            Ready to Stop Working Harder and Start Working Smarter?
          </h2>
          <p className="mt-4 text-lg text-emerald-100 max-w-xl mx-auto leading-relaxed">
            Get instant access to every tool you need to save hours, stay organized, and grow your solo business.
          </p>

          <div className="mt-10">
            <Button
              size="lg"
              className="bg-white text-emerald-700 hover:bg-emerald-50 font-bold px-10 py-4 text-lg rounded-xl shadow-xl"
            >
              Get the All-Access Bundle — $189
              <ArrowRight className="ml-2 h-5 w-5" />
            </Button>
            <p className="mt-4 text-sm text-emerald-200">
              30-day money-back guarantee &bull; Instant download &bull; Lifetime access
            </p>
          </div>

          <div className="mt-10 flex flex-wrap items-center justify-center gap-6 text-sm text-emerald-200">
            <button
              onClick={() => scrollTo('products')}
              className="hover:text-white transition-colors underline underline-offset-4 decoration-emerald-400/40 hover:decoration-emerald-300"
            >
              AI Prompt Pack — $49
            </button>
            <button
              onClick={() => scrollTo('products')}
              className="hover:text-white transition-colors underline underline-offset-4 decoration-emerald-400/40 hover:decoration-emerald-300"
            >
              Solo Ops Playbook — $79
            </button>
            <button
              onClick={() => scrollTo('products')}
              className="hover:text-white transition-colors underline underline-offset-4 decoration-emerald-400/40 hover:decoration-emerald-300"
            >
              Launch Marketing Kit — $99
            </button>
          </div>
        </div>
      </section>

      {/* ═══════ FOOTER ═══════ */}
      <footer className="bg-slate-900 text-slate-400 py-12">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col md:flex-row items-center justify-between gap-8">
            <div className="text-center md:text-left">
              <div className="flex items-center justify-center md:justify-start gap-2 mb-2">
                <Package className="h-5 w-5 text-emerald-500" />
                <span className="text-lg font-bold text-white">
                  Solo<span className="text-emerald-500">GrowthKit</span>
                </span>
              </div>
              <p className="text-sm">The growth toolkit for solo founders.</p>
            </div>

            <div className="flex flex-wrap items-center justify-center gap-6 text-sm">
              <button
                onClick={() => scrollTo('products')}
                className="hover:text-white transition-colors"
              >
                Products
              </button>
              <button
                onClick={() => scrollTo('faq')}
                className="hover:text-white transition-colors"
              >
                FAQ
              </button>
              <span className="text-slate-600">Privacy Policy</span>
              <span className="text-slate-600">Terms of Service</span>
              <span className="text-slate-600">Refund Policy</span>
              <span className="text-slate-600">Contact</span>
            </div>
          </div>

          <Separator className="my-8 bg-slate-800" />

          <div className="text-center text-xs text-slate-500 space-y-1">
            <p>&copy; 2026 SoloGrowthKit. All rights reserved.</p>
            <p>This is a sole proprietorship. All digital products are protected by copyright.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}
