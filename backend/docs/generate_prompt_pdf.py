from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
import os

file_path = "c:/Users/YUVARAJ/OneDrive/Desktop/Agency/digital_agency_backend_prompt.pdf"

styles = getSampleStyleSheet()
title_style = styles["Title"]
heading_style = styles["Heading2"]
text_style = styles["BodyText"]

title = "Comprehensive Development Prompt for Digital Agency Website Backend and Feature Enhancements"

sections = [
("Introduction",
"""You are an expert senior full-stack software engineer responsible for designing, debugging, and improving a modern digital agency website platform. The project belongs to a digital marketing and web development agency called “BhAAi Fans Digital AA”. The system currently includes a frontend website and a backend server built using Python Flask and SQLite. However, several problems and missing features exist that must be fixed and redesigned professionally.

Your task is to analyze the existing system and generate a complete, production-ready architecture and implementation plan that resolves the issues in the website, improves the user experience, secures the backend administration panel, and implements a full lead management system. The final system must allow visitors to browse the website, request services, create accounts, and send messages to the agency, while the admin can securely access a private backend panel to manage leads and communications.

This prompt describes all requirements that must be implemented and fixed in the project. The generated solution must include backend logic, frontend fixes, authentication flows, database storage, and secure communication between the website and the admin dashboard. The final architecture must be modular, scalable, and easy to maintain."""),

("Image Loading Issue Fix",
"""One of the primary problems in the current website is that images are not loading correctly. The frontend displays sections such as Selected Works, agency portfolio previews, team images, and marketing banners, but these images appear broken or blank. This happens because the static asset paths are not configured properly between the frontend and backend.

The solution must correct how images and static assets are served. The backend Flask application must correctly expose the static assets directory. All image URLs must reference the correct static path. The folder structure should separate images, stylesheets, scripts, and fonts inside a unified assets directory.

The backend should serve images through a dedicated route that ensures the browser can retrieve them properly. The frontend HTML must use consistent paths such as /assets/images/... instead of relative paths that break when routing occurs. The system should support multiple image categories including portfolio images, team photos, icons, logos, and background graphics.

Additionally, the backend must ensure caching headers and optimized delivery so that images load efficiently. The corrected implementation must guarantee that all images in sections like Selected Works, About Us, and Services display correctly on every page."""),

("Homepage Quote Feature",
"""At the beginning of the homepage, the design includes an empty space on the left side that should contain a motivational or branding quote. Currently this section is blank and does not provide any meaningful content.

The system must introduce a dynamic quote component that displays inspirational quotes related to creativity, technology, innovation, and digital marketing. These quotes should appear visually appealing and align with the branding style of the agency.

The quotes can be stored in the backend database or generated through a backend API endpoint. When the homepage loads, the frontend should fetch a quote from the backend using an API request and render it inside the hero section.

The quote section should support rotation or randomization so that visitors see different quotes each time they load the website. This feature will improve engagement and create a stronger visual introduction to the brand.

Styling should ensure the quote text appears prominently on the left side of the hero section with appropriate typography, spacing, and contrast. The quote must complement the main headline of the page rather than distracting from it."""),

("Private Backend Admin Website",
"""The system must include a completely separate backend website used only by the agency owner or administrators. This backend interface must function as a private admin dashboard and should never be accessible publicly without authentication.

The admin website should include a login page where administrators can enter credentials to access the system. Once logged in, the admin will see a dashboard displaying leads, messages, analytics, and service inquiries submitted through the public website.

Security is extremely important. The admin routes must be protected using authentication middleware. If a user tries to access the admin dashboard without logging in, the system must block access and return an unauthorized response.

The backend dashboard must provide features such as viewing messages from clients, reading contact requests, filtering leads, deleting spam entries, and monitoring statistics like total inquiries received. This panel acts as the command center for managing the agency’s incoming client communication."""),

("User Contact and Account System",
"""Another requirement is implementing a proper account system for visitors who want to contact the agency. When a user clicks the “Get in Touch” button or attempts to send a message through the contact form, the system must require authentication.

If the visitor already has an account, they should be able to log in using their email and password. If the visitor does not yet have an account, the system must provide a registration form that allows them to create a new account before submitting their inquiry.

The account creation process should collect basic information such as name, email address, and password. Passwords must be securely stored using hashing mechanisms to protect user credentials.

Once logged in, the user can submit contact requests, project inquiries, or service requirements. These messages should be stored in the database and associated with the user’s account so that the admin can see who submitted each request.

The authentication system must include login, registration, logout, and session management functionality."""),

("Email Notification System",
"""Every time a user submits a contact message or service inquiry, the system must automatically send an email notification to the agency owner. The email address for receiving these messages is yuvarajdevarakonda24@gmail.com.

The backend must integrate with an email delivery system using SMTP or a transactional email service. When a new message is received, the backend should format an email containing the sender’s name, email address, requested service, and message content.

This email should be sent instantly to the specified mailbox so that the agency owner is notified in real time whenever a new lead arrives. The email content should be clearly formatted and professional so it can be quickly reviewed.

This feature ensures that important client requests are not missed even if the admin dashboard is not currently open."""),

("Lead Storage and Backend Display",
"""All user inquiries must also be stored in the system database. The database should contain tables for users, leads, services, and messages. When a visitor submits a request, the system must store the message along with metadata such as timestamp, user ID, and service category.

Inside the admin dashboard, these leads should appear in a structured table showing the client’s name, email address, requested service, and message description. The admin must be able to review each lead and manage them efficiently.

The dashboard should also display simple statistics such as the total number of inquiries, the most requested services, and the most recent messages. This will help the agency understand client demand and track business growth."""),

("Expected Final Outcome",
"""The final system must operate as a fully functional digital agency platform. Visitors can explore the website, view portfolio work, and learn about the services offered by the agency. When they want to contact the agency, they must first authenticate or create an account.

Once authenticated, they can submit their project requirements through a contact form. The backend will store the information in the database, send an email notification to the agency owner, and display the request in the private admin dashboard.

The admin can log in securely, view all incoming leads, manage messages, and monitor statistics. Static assets such as images will load correctly, the homepage will display motivational quotes, and the overall system will provide a professional experience for both visitors and administrators.

The implementation should follow best practices for backend architecture, database design, authentication security, and frontend integration."""),
]

story = []
story.append(Paragraph(title, title_style))
story.append(Spacer(1,20))

for heading, text in sections:
    story.append(Paragraph(heading, heading_style))
    story.append(Spacer(1,10))
    for para in text.split("\n\n"):
        story.append(Paragraph(para.strip(), text_style))
        story.append(Spacer(1,10))
    story.append(Spacer(1,10))

doc = SimpleDocTemplate(file_path, pagesize=A4, rightMargin=72,leftMargin=72, topMargin=72,bottomMargin=72)
doc.build(story)

print(file_path)
