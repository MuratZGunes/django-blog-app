# Django Blog Uygulaması
[![English](https://img.shields.io/badge/Language-English-blue)](https://github.com/MuratZGunes/django-blog-app/blob/main/README.md)

Bu proje, Django framework'ü kullanılarak geliştirilmiş bir blog uygulamasıdır. Kullanıcılar makale oluşturabilir, düzenleyebilir, silebilir ve yorum yapabilir. Ayrıca, kullanıcı kayıt ve oturum açma işlemleri desteklenmektedir.

## Özellikler

- Kullanıcı kayıt, giriş ve çıkış işlemleri
- Makale oluşturma, güncelleme ve silme
- Makale detay sayfasında yorum ekleyebilme
- Makale ve yorumlar için dinamik içerik yönetimi
- Zengin metin düzenleyici (CKEditor) entegrasyonu
- Bootstrap 5 ile modern ve duyarlı tasarım

## Kurulum

### 1. Depoyu Klonlayın

```bash
git clone https://github.com/MuratZGunes/django-blog-app.git
cd django-blog-app
```

### 2. Sanal Ortam Oluşturun

```bash
python -m venv env
source env/bin/activate # Linux/MacOS
env\Scripts\activate # Windows
```

### 3. Gerekli Paketleri Yükleyin

```bash
pip install -r requirements.txt
```

### 4. Veritabanını Hazırlayın

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Admin Kullanıcısı Oluşturun

```bash
python manage.py createsuperuser
```

### 6. Statik Dosyaları ve Ortam Dosyalarını Ayarlayın

```bash
python manage.py collectstatic
```

### 7. Sunucuyu Başlatın

```bash
python manage.py runserver
```

Tarayıcınızdan uygulamayı şu adresten ziyaret edin:

```
http://127.0.0.1:8000/
```

## Kullanılan Teknolojiler

- Django 5.1.4
- SQLite (varsayılan veritabanı)
- CKEditor
- Crispy Forms (Bootstrap 5)
- Python 3.x
- HTML, CSS, Bootstrap 5

## Proje Yapısı

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

## Ekran Görüntüleri

### Ana Sayfa

![blmainpage](https://github.com/user-attachments/assets/9e81089e-bf3f-4039-8e28-4406700dca25)


### Makale Detay Sayfası

  ![blogdetailpage](https://github.com/user-attachments/assets/cd35a909-80b5-43ae-ad40-de5fc43e4f0e)


### Kontrol Paneli
![blogdashboard](https://github.com/user-attachments/assets/e4377118-77a9-4d89-b246-4add1582fb5d)

##
---
Herhangi bir sorun veya öneriniz için benimle [GitHub](https://github.com/MuratZGunes/django-blog-app) üzerinden iletişime geçebilirsiniz!

