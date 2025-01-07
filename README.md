# Django Blog Application
[![Turkish](https://img.shields.io/badge/Dil-Türkçe-blue)](https://github.com/MuratZGunes/django-blog-app/tree/main/README_TR.md)

This project is a blog application developed using the Django framework. Users can create, edit, delete, and comment on articles. Additionally, user registration and login functionalities are supported.

## Features

- User registration, login, and logout operations
- Creating, updating, and deleting articles
- Adding comments on article detail pages
- Dynamic content management for articles and comments
- Rich text editor (CKEditor) integration
- Modern and responsive design with Bootstrap 5

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/MuratZGunes/django-blog-app.git
cd django-blog-app
```

### 2. Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate # Linux/MacOS
env\Scripts\activate # Windows
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Prepare the Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create an Admin User

```bash
python manage.py createsuperuser
```

### 6. Configure Static and Media Files

```bash
python manage.py collectstatic
```

### 7. Start the Server

```bash
python manage.py runserver
```

Visit the application in your browser at:

```
http://127.0.0.1:8000/
```

## Technologies Used

- Django 5.1.4
- SQLite (default database)
- CKEditor
- Crispy Forms (Bootstrap 5)
- Python 3.x
- HTML, CSS, Bootstrap 5

## Project Structure

```
├── blog
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── ...
├── article
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── ...
├── user
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── ...
├── templates
│   ├── layout.html
│   ├── index.html
│   ├── dashboard.html
│   ├── articles.html
│   ├── ...
└── static
    ├── css
    ├── js
    └── ...
```

## Screenshots

### Home Page

![blmainpage](https://github.com/user-attachments/assets/c7881bda-1bb4-4d80-82c2-42a55805f3a3)


### Article Detail Page

![blogdetailpage](https://github.com/user-attachments/assets/e8365a08-17a0-435d-acbb-70f9ac785395)


### Dashboard
![blogdashboard](https://github.com/user-attachments/assets/250d2454-f019-489e-87a5-19c35829784c)

##

### Articles Page

![blogarticles](https://github.com/user-attachments/assets/5b3ed0ea-c508-4c6d-86c4-2f3ff888bb50)

##

---
For any questions or suggestions, feel free to contact me via [GitHub](https://github.com/MuratZGunes/django-blog-app)!

