# URL Shortener (Django)

A simple Django-based URL shortener that allows users to shorten long URLs and redirect to the original links using the generated short codes.

## Features

- Shortens long URLs into a unique short code.
- Redirects users to the original URL when they visit the shortened URL.
- Generates random short codes for URLs.
- Stores URLs and short codes in a database (using SQLite or any other database supported by Django).

## Technologies Used

- **Django**: The web framework used for building the URL shortener.
- **SQLite**: Default database (you can switch to PostgreSQL, MySQL, etc.).
- **Python**: Programming language used to write the project.

## Getting Started

### Prerequisites

Ensure that you have the following installed on your local development machine:

- Python 3.x
- Django
- Git

### Setup Instructions

1. **Clone the Repository**

   First, clone the repository to your local machine using Git:

   ```bash
   git clone https://github.com/yourusername/url-shortener-django.git
   ```

2. **Navigate to the Project Directory**

   Move into the project directory:

   ```bash
   cd url-shortener-django
   ```

3. **Create and Activate Virtual Environment**

   Create a Python virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate  # Windows
   ```

4. **Install Dependencies**

   Install all the dependencies listed in the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Database Migrations**

   Set up the database by applying the migrations:

   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

7. **Visit the Application**

   Open a browser and visit:

   ```
   http://localhost:8000
   ```

### Creating a Shortened URL

- Enter a long URL in the provided form, and the app will generate a short code.
- You will be provided with a shortened URL, which you can share or use to redirect to the original URL.

### Redirecting to the Original URL

To use the shortened URL, visit:

```
http://localhost:8000/<short_code>
```

This will redirect you to the original URL associated with the short code.

## Project Structure

```
url_shortener/
├── manage.py
├── shortener/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
├── templates/
│   └── shortener/
│       ├── home.html
│       └── success.html
├── url_shortener/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
└── README.md
```

## Future Improvements

- Allow users to create custom short codes.
- Implement user authentication to track personalized short links.
- Add analytics for the number of times a short URL has been visited.

## License

This project is open-source and available under the [MIT License](LICENSE).
