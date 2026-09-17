import type { Metadata } from "next";
import { Outfit } from "next/font/google";
import "./globals.css";
import { AppProvider } from "@/context/AppContext";

const outfit = Outfit({
  variable: "--font-outfit",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "JogjaVisit - Eksplorasi Wisata, Rental, & Kuliner",
  description: "Platform rekomendasi terintegrasi untuk wisatawan di Daerah Istimewa Yogyakarta.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="id">
      <body
        className={`${outfit.variable} antialiased bg-white dark:bg-slate-900 transition-colors duration-300 text-slate-900 dark:text-white`}
      >
        <AppProvider>
          {children}
        </AppProvider>
      </body>
    </html>
  );
}
