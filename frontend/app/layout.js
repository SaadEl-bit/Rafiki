import "./globals.css";

export const metadata = {
  title: "Rafiki - Ton compagnon pour le Bac",
  description: "Personalized paths and 24/7 automated tutoring for Moroccan students.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en" className="light">
      <head>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@700&display=swap" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" />
      </head>
      <body className="bg-background text-on-surface font-body-md min-h-screen selection:bg-primary selection:text-on-primary">
        {children}
      </body>
    </html>
  );
}
