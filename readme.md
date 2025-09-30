Uni ERP - University Management System
Table of Contents

Project Overview

Tech Stack

Features Implemented

Current Status

Setup & Installation

Usage

Future Updates

Contributing

License

Project Overview

Uni ERP is a fully-featured University Enterprise Resource Planning (ERP) System built with Django. It centralizes management of academics, finance, exams, enrollments, timetables, and user authentication.
The system is designed to be modular, scalable, and secure, with both template-based views for administrative staff and REST APIs for integration with other services.

Tech Stack

Backend: Django 5.2, Django REST Framework (DRF)

Frontend: Django Templates, Tailwind CSS

Database: PostgreSQL / SQLite (for testing)

Authentication: Django's built-in authentication system (custom User model)

Optional: DRF JWT for API authentication

Features Implemented
1. User Management

Custom User model integrated.

Template-based views:

Login

Logout

User creation (popup-enabled)

User list, detail, edit, delete

Future-ready API endpoints for User CRUD.

2. Academics Module

Departments: CRUD operations

Courses: CRUD operations with department link

Sections: CRUD operations with teacher assignment

Fully integrated template views and URL routing.

DRF-ready API views (commented out for now)

3. Finance Module

Fees, Payments, Scholarships, Fines (templates implemented)

CRUD operations

PDF reports (optional)

4. Enrollment & Exams

Enrollment model: enroll/drop courses

Exam & Result management with auto-grading

Templates for listing, adding, updating, and deleting exams

Popup-based user creation in templates

5. Authentication Enhancements

Custom login/logout views

Register popup after first login (optional)

CSRF-safe forms

Login-required decorators and class-based mixins

Current Status

Core modules (Academics, Accounts, Exams, Finance) implemented

Template views and forms fully functional

Base template with responsive navigation

Pop-up registration system for admin users

REST APIs ready but currently commented out

Basic CSRF protection added

Setup & Installation
# Clone the repository
git clone https://github.com/username/uni-erp.git
cd uni-erp

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

Usage

Access the system at http://127.0.0.1:8000/

Login via /accounts/login/

Admin users can create new users using the popup in the navbar.

Navigate through Academics, Finance, Exams, and Enrollments via the dashboard.

All actions require authentication.

Future Updates

Planned enhancements for a fully automated ERP:

Attendance Management: Integrate automated attendance tracking.

Timetable Management: Auto-generate class schedules.

Notifications: Email/SMS alerts for fees, exam results, deadlines.

Analytics Dashboard: Visual reports for academics, finance, and enrollment.

API Integration: JWT-secured REST API for mobile apps.

Role-based Access: Granular permissions for Admin, Teacher, Student.

AI-Powered Features: Smart suggestions for courses, scholarships, and academic performance.

Payment Gateway Integration: Online fee payment and receipts.

Document Management: Upload/download notices, timetables, and exam schedules.

Contributing

Contributions are welcome!

Fork the repository

Create a new branch (git checkout -b feature/new-feature)

Commit changes (git commit -am 'Add new feature')

Push to the branch (git push origin feature/new-feature)

Open a Pull Request