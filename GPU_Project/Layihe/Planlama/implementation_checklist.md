# Portfolio Layihəsi - İcra Checklist

## Başlanğıc Setup (Gün 1)

### Next.js Layihəsini Başlat:
```bash
npx create-next-app@latest portfolio --typescript --tailwind --app
cd portfolio
```

### Əsas Dependencies:
```bash
npm install @supabase/supabase-js
npm install react-icons
npm install framer-motion
npm install @emailjs/browser
npm install react-hook-form
npm install @headlessui/react
```

### Layihə Strukturu:
```
portfolio/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   ├── about/page.tsx
│   ├── projects/page.tsx
│   ├── contact/page.tsx
│   └── admin/
│       ├── layout.tsx
│       └── page.tsx
├── components/
│   ├── Header.tsx
│   ├── Footer.tsx
│   ├── ProjectCard.tsx
│   ├── ContactForm.tsx
│   └── ThemeToggle.tsx
├── lib/
│   ├── supabase.ts
│   └── types.ts
├── data/
│   └── projects.json
└── public/
    └── images/
```

## MVP Features Checklist:

### Ana Səhifə:
- [ ] Hero section with animation
- [ ] Brief introduction
- [ ] Featured projects (3-4)
- [ ] CTA buttons

### Haqqımda:
- [ ] Personal info section
- [ ] Skills with progress bars
- [ ] Education/Certifications
- [ ] Download CV button

### Portfolio:
- [ ] Project grid layout
- [ ] Filter by technology
- [ ] Project modal/detail view
- [ ] Live demo & GitHub links

### Əlaqə:
- [ ] Contact form
- [ ] Social media links
- [ ] Email/Phone display
- [ ] Form validation

### Ümumi Features:
- [ ] Responsive navbar
- [ ] Dark/Light mode toggle
- [ ] Smooth scrolling
- [ ] Loading states
- [ ] 404 page
- [ ] SEO meta tags

## Deployment Checklist:

### Vercel Setup:
- [ ] Connect GitHub repo
- [ ] Configure environment variables
- [ ] Setup custom domain
- [ ] Enable analytics

### Supabase Setup:
- [ ] Create project
- [ ] Setup tables (projects, messages)
- [ ] Configure Row Level Security
- [ ] Setup storage bucket

### Final Checks:
- [ ] Test all forms
- [ ] Check responsive design
- [ ] Validate SEO
- [ ] Performance audit
- [ ] Security headers
