# Django Image Uploader

A beginner-friendly Django project that demonstrates how to upload, store, and display images using Django and MySQL. This project covers Django file handling with `ImageField`, `MEDIA_ROOT`, and `MEDIA_URL`, along with a responsive Bootstrap-based user interface.

## 🚀 Features

- Upload images with titles
- Store image metadata in MySQL
- Save uploaded images in the `media/` directory
- Display uploaded images in a responsive gallery
- Django ModelForm for image uploads
- Bootstrap 5 responsive UI
- Django Admin support
- Beginner-friendly project structure

## 🛠️ Tech Stack

- Python 3.x
- Django 5.x
- MySQL
- HTML5
- CSS3
- Bootstrap 5
- Pillow

## 📂 Project Structure

```
django-image-uploader/
│
├── media/
├── static/
├── templates/
│   ├── base.html
│   ├── upload.html
│   └── gallery.html
│
├── image_app/
│   ├── migrations/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── image_uploader/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/django-image-uploader.git
cd django-image-uploader
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure MySQL

Create a MySQL database and update the `DATABASES` configuration in `settings.py`.

Example:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'image_gallery',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 6. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 8. Run the server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

## 📸 Image Upload

This project uses Django's `ImageField` to upload images.

Uploaded files are stored in the `media/` directory.

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

During development, media files are served by Django using:

```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
```

## 📦 Requirements

```
Django
Pillow
mysqlclient
```

Install them using:

```bash
pip install Django Pillow mysqlclient
```

## 🎯 Learning Outcomes

This project helped me learn:

- Django project structure
- Models and Django ORM
- Forms and ModelForms
- File uploads with `ImageField`
- `request.FILES`
- `MEDIA_ROOT` and `MEDIA_URL`
- MySQL integration
- Django Migrations
- Bootstrap integration
- Django Admin

## 📄 License

This project is created for educational purposes.

Sample images used in this project are licensed as **Free for Commercial Use** and **No Attribution Required** from Pixabay.

## 👩‍💻 Author

**Naga Reethika Ravi**

- GitHub: https://github.com/NagaReethika
- LinkedIn: https://linkedin.com/in/naga-reethika-ravi-a7623a226
