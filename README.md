# BhAAi Fans Digital AA — Website

**Web, Marketing & Creative Solutions for Modern Brands**

---

## Project Structure

```
digital-agency-website/
├── frontend/
│   ├── pages/          ← Main HTML pages (index, about, services, portfolio, pricing, contact)
│   ├── services/       ← Individual service detail pages (6 pages)
│   ├── css/            ← Stylesheets (style.css, services.css, responsive.css)
│   ├── js/             ← JavaScript (main.js, form.js, animations.js)
│   ├── images/         ← Logos, portfolio images, icons (add your own)
│   └── assets/         ← Videos and graphics
├── backend/
│   ├── app.py          ← Flask entry point
│   ├── routes/         ← API route handlers
│   ├── models/         ← SQLite database models
│   ├── database/       ← SQLite database file (auto-created)
│   ├── uploads/        ← File uploads directory
│   └── utils/          ← Email service and validation helpers
├── admin-dashboard/    ← Internal admin panel (dashboard, clients, requests)
├── docs/               ← Project documentation
├── requirements.txt
├── .env                ← Environment variables (never commit this)
└── README.md
```

---

## Getting Started

### 1. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure environment
Edit `.env` with your SMTP credentials and secret key.

### 3. Run the backend
```bash
cd backend
python app.py
```

### 4. Open the frontend
Open `frontend/pages/index.html` in your browser, or serve via Flask's static files.

---

## Services Offered
1. Web Development
2. Social Media Marketing
3. Ads Management
4. Video Editing
5. Graphic Design
6. Marketing Strategy

---

## Adding Your Images
Place your images in:
- `frontend/images/logos/` — Agency logo files
- `frontend/images/portfolio/` — Portfolio project screenshots
- `frontend/images/icons/` — UI icons

---

## Customisation
- **Colors:** Edit CSS variables in `frontend/css/style.css` (`:root` block)
- **Content:** Update text directly in HTML files under `frontend/pages/`
- **Pricing:** Edit the pricing cards in `frontend/pages/pricing.html`
- **Email:** Set SMTP credentials in `.env`

---

## Tech Stack
- **Frontend:** Vanilla HTML, CSS (custom design system), JavaScript
- **Backend:** Python / Flask
- **Database:** SQLite (via Python's sqlite3)
- **Fonts:** Bebas Neue + DM Sans + DM Mono (Google Fonts)

---

© 2025 BhAAi Fans Digital AA · Hyderabad, Telangana, India
