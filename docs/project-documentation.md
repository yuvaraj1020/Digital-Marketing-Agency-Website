# BhAAi Fans Digital AA — Project Documentation

## Overview
Full-stack digital agency website built with a dark, editorial aesthetic inspired by premium design studios.

## Design System
- **Primary font:** Bebas Neue (display/headings)
- **Body font:** DM Sans (body text)
- **Mono font:** DM Mono (labels, tags, nav)
- **Background:** #0a0a0a (near-black)
- **Primary text:** #f5f0e8 (warm off-white)
- **Accent:** #c8ff00 (lime green)

## Pages
| File | URL | Description |
|------|-----|-------------|
| `pages/index.html` | / | Homepage with hero, services, portfolio, FAQ |
| `pages/about.html` | /about | Studio / About page |
| `pages/services.html` | /services | All 6 services overview |
| `pages/portfolio.html` | /portfolio | Filterable portfolio grid |
| `pages/pricing.html` | /pricing | 3-tier pricing cards |
| `pages/contact.html` | /contact | Contact form with validation |

## Service Pages
Each service has its own detail page under `services/`:
- `web-development.html`
- `social-media-marketing.html`
- `ads-management.html`
- `video-editing.html`
- `graphic-design.html`
- `marketing-strategy.html`

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/contact | Submit contact form |
| POST | /api/service-request | Create service request |
| GET | /api/service-requests | List all requests (admin) |
| POST | /api/video-upload | Upload video file |
| POST | /api/marketing-enquiry | Submit marketing enquiry |
| GET | /api/health | Health check |

## JavaScript Features
- Custom cursor (dot + follower ring)
- Page intro animation
- Scroll-based reveal animations (IntersectionObserver)
- FAQ accordion
- Mobile navigation menu
- Counter animations
- Magnetic button effect
- Text scramble hover on labels
- Parallax hero background

## Form Validation
Validated fields on contact form:
- name (required)
- email (required, format checked)
- phone (optional, format checked if provided)
- service (required, select)
- message (required, min 10 chars)

## Deployment Notes
- Backend: `gunicorn backend.app:app` for production
- Set `FLASK_ENV=production` in `.env`
- Change `SECRET_KEY` to a secure random string
- Configure SMTP credentials for email notifications
- Database auto-initialises on first request
