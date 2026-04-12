import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import { Toaster } from "@/components/ui/toaster";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "SoloGrowthKit — The Growth Toolkit for Solo Founders",
  description:
    "500+ proven AI prompts, ready-to-use business templates, and marketing playbooks built specifically for solo founders who need to do more with less.",
  keywords: [
    "solo founder",
    "freelancer",
    "solopreneur",
    "AI prompts",
    "business templates",
    "marketing playbook",
    "digital products",
    "SoloGrowthKit",
  ],
  authors: [{ name: "SoloGrowthKit" }],
  openGraph: {
    title: "SoloGrowthKit — The Growth Toolkit for Solo Founders",
    description:
      "500+ proven AI prompts, ready-to-use business templates, and marketing playbooks built specifically for solo founders who need to do more with less.",
    siteName: "SoloGrowthKit",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "SoloGrowthKit — The Growth Toolkit for Solo Founders",
    description:
      "500+ proven AI prompts, ready-to-use business templates, and marketing playbooks built specifically for solo founders.",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="scroll-smooth" suppressHydrationWarning>
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased bg-white text-slate-900`}
      >
        {children}
        <Toaster />
      </body>
    </html>
  );
}
