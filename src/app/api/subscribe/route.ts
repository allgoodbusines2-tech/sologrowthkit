import { NextRequest, NextResponse } from 'next/server'
import { db } from '@/lib/db'

export async function POST(request: NextRequest) {
  try {
    const body = await request.json()
    const { name, email } = body

    if (!email || typeof email !== 'string') {
      return NextResponse.json(
        { error: 'Email is required' },
        { status: 400 }
      )
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!emailRegex.test(email)) {
      return NextResponse.json(
        { error: 'Please provide a valid email address' },
        { status: 400 }
      )
    }

    const lead = await db.lead.create({
      data: {
        name: name || null,
        email: email.trim().toLowerCase(),
      },
    })

    return NextResponse.json(
      {
        success: true,
        message: 'Successfully subscribed!',
        lead: { id: lead.id, email: lead.email },
      },
      { status: 201 }
    )
  } catch (error: unknown) {
    const err = error as { code?: string; message?: string }
    if (err.code === 'P2002') {
      return NextResponse.json(
        { error: 'This email is already subscribed. Thank you for your interest!' },
        { status: 409 }
      )
    }
    console.error('Subscribe error:', error)
    return NextResponse.json(
      { error: 'Something went wrong. Please try again.' },
      { status: 500 }
    )
  }
}
