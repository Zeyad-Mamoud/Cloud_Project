Loan Tracking System

A system to track personal loans (borrowed or lent) with features to:

Add a new loan with amount and due date.

Link a loan to a contact.

Mark a loan as paid or partially repaid.

Receive automatic reminders.

Setup

Backend

Navigate to backend/.

Install dependencies: pip install -r requirements.txt.

Run with Docker: docker-compose up.

Frontend

Navigate to frontend/.

Install dependencies: npm install.

Start development server: npm start.

Deployment

Backend: Deploy to Heroku with Dockerfile.

Frontend: Deploy to Netlify or Vercel.

Architecture

Follows Clean Architecture with layers:

Domain: Entities and Repositories.

Application: Use Cases.

Infrastructure: API and Database.

Presentation: React frontend.
