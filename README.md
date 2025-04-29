# Movie Review Django Project

This is a Django-based web application for reviewing movies. Users can add movies, write reviews, and manage profiles.

## Features

- User registration and login
- Add and manage movies
- Write and edit reviews
- User profiles
- Responsive UI with templates and static files

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Khalyyl/django.git
   cd django
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000/`

## Usage

- Register a new user or login with existing credentials.
- Add movies and write reviews.
- Manage your profile.

## Running Tests

To run tests, use:
```bash
python manage.py test
```

## License

This project is licensed under the MIT License.
