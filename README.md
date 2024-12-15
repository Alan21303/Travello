Travello

Travello is a web application built with HTML, CSS, JavaScript, and Django. This project aims to create a travel-oriented website to showcase destinations, provide travel-related information, and engage users with a visually appealing interface.

Current Features

Homepage: A responsive landing page with navigation to various sections.

About Page: Details about the travel services offered.

Destinations Page: A list of popular travel destinations.

News Page: Recent travel news and updates.

Contact Page: A form to collect inquiries or feedback from users.

Directory Structure

travelWebsite/
├── assets/          # Contains static assets like images, stylesheets, and scripts
├── MainApp/         # Django application directory
│   ├── migrations/  # Database migration files
│   ├── __pycache__/ # Compiled Python files
│   ├── admin.py     # Admin panel configuration
│   ├── apps.py      # Application configuration
│   ├── models.py    # Data models (currently empty)
│   ├── tests.py     # Test cases
│   ├── urls.py      # URL routing for the app
│   └── views.py     # Logic for handling web requests
├── static/          # Folder for static files
├── templates/       # HTML templates
│   ├── admin/       # Admin panel templates
│   ├── pages/       # Page-specific templates
│   ├── partials/    # Reusable partial components
│   ├── about.html   # About page template
│   ├── base.html    # Base layout template
│   ├── contact.html # Contact page template
│   ├── destinations.html # Destinations page template
│   ├── elements.html # Miscellaneous elements template
│   ├── index.html   # Homepage template
│   └── news.html    # News page template
├── travelWebsite/   # Project configuration folder
│   ├── __pycache__/ # Compiled Python files
│   ├── asgi.py      # ASGI configuration
│   ├── settings.py  # Project settings
│   ├── urls.py      # Project-level URL configuration
│   ├── wsgi.py      # WSGI configuration
│   └── __init__.py  # Python package initializer
├── db.sqlite3       # SQLite database (auto-generated)
├── manage.py        # Django management script
└── README.md        # Project documentation

How to Run the Project

Clone the repository:

git clone https://github.com/Alan21303/Travello.git

Navigate to the project directory:

cd travelWebsite

Install the required Python packages:

pip install django

Run the development server:

python manage.py runserver

Open your browser and go to http://127.0.0.1:8000/ to view the application.

Future Enhancements

Add database integration for dynamic content.

Implement user authentication.

Enhance the design with additional interactive elements.

Add functionality for user reviews and ratings for destinations.

License

This project is open-source and available under the MIT License.
