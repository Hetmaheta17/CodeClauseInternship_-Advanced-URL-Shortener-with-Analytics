# URL Shortener Project

Welcome to the URL Shortener, a powerful and user-friendly web application that allows users to shorten long URLs into easily shareable links. This project is built using Django, Tailwind CSS, and a robust database backend to ensure seamless performance and tracking.

# Features

User Authentication

Register and login with secure credentials.

Password hashing and authentication using Django's built-in security features.

URL Shortening

Convert long URLs into short, easy-to-remember links.

Custom short URLs with tracking capabilities.

Analytics & Tracking

Track the number of clicks on each shortened URL.

View detailed analytics, including timestamps and visitor insights.

User Dashboard

Manage shortened links via an intuitive dashboard.

Edit or delete URLs with ease.

Responsive & Aesthetic UI

Designed using Tailwind CSS for a sleek and modern interface.

Fully responsive for mobile and desktop users.

# Installation

Follow these steps to set up the project locally:

Prerequisites

Ensure you have the following installed:

Python 3.12+

Django 5.1+

SQLite or PostgreSQL (as per your choice)

Setup Instructions

Clone the Repository:

git clone https://github.com/Hetmaheta17/CodeClauseInternship_-Advanced-URL-Shortener-with-Analytics.git

cd url-shortener

Create a Virtual Environment:

python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

Install Dependencies:

pip install -r requirements.txt

Run Migrations:

python manage.py makemigrations
python manage.py migrate

Run the Development Server:

python manage.py runserver

Access the Application:
Open http://127.0.0.1:8000 in your web browser.

# Usage

Navigate to the homepage.

Register/Login to create an account.

Enter a long URL and generate a short link.

Share the shortened link and track its analytics.

Manage your links via the dashboard.

# Project Structure

url-shortener/
│-- shortener/            # Django app containing models, views, and templates
│-- static/               # Static files (CSS, JS, images)
│-- templates/            # HTML templates
│-- url_shortener/         # Project settings and URLs
│-- .venv/                 # Virtual environment (ignored in Git)
│-- manage.py              # Django management commands
│-- requirements.txt       # Dependencies
│-- README.md              # Project documentation

# Technologies Used

Backend: Django (Python)

Frontend: Tailwind CSS

Database: SQLite/PostgreSQL

Deployment: Gunicorn, Nginx (for production)

# Contributing

We welcome contributions! Follow these steps to contribute:

Fork the repository.

Create a new branch (feature-branch).

Commit your changes with meaningful messages.

Submit a pull request.

# Contact

For any queries or feedback, feel free to reach out:

Email: hetmaheta17@gmail.com

GitHub: Hetmaheta17

Thank you for using URL Shortener! 🚀

