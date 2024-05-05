# Django CRM

Django CRM is a customer relationship management system built using Django.

## Features

- **User Authentication**:
  - User registration.
  - Login and logout functionality.

- **Customer Management**:
  - Add, update, and delete customer records.
  - View customer details and history.

## Installation

### Prerequisites

- Python 3.x
- Django
- Virtualenv (recommended)

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/AflaxCade/Django-CRM.git
```

2. Navigate to the project directory:

```bash
cd Django-CRM
```


3. Create a virtual environment:

```bash
python -m venv env
```

4. Activate the virtual environment:

- For Windows:

```bash
env\Scripts\activate
```

- For macOS and Linux:

```bash
source env/bin/activate
```

5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

6. Apply Migrations:

```bash
python manage.py migrate
```

7. Create Superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to create a superuser account.

8. Run the Development Server:

```bash
python manage.py runserver
```

The server will start on `http://localhost:8000` or `http://127.0.0.1:8000`.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b  feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
