# Django Uygulaması

Bu proje, Django ile geliştirilmiş bir web uygulamasıdır. Uygulama hem lokal ortamda hem de Docker üzerinden çalıştırılabilir. Ayrıca **Swagger** ile API dokümantasyonu sağlanmıştır. Örnek **Test** api'leri vardır. Örnek **action** metodları vardır

## Özellikler

- Django framework kullanılarak geliştirilmiştir.
- PostgreSQL veritabanı kullanır.
- Docker ve Docker Compose
- Swagger

## Gereksinimler

- Python 3.10
- Docker & Docker Compose
- PostgreSQL

## Kurulum

### Local Ortamda Çalıştırma

1. **Proje requirements:**

   ```bash
   pip install -r requirements.txt

2. **Veritabanı local için:**
    - settings.py içinde bulunan database dict üzerindeki host değeri "localhost" olmalı      
  
3. **Migration:**
      ```bash
      python manage.py migrate

4. **Run:**
     ```bash
      python manage.py runserver


### Dockerda Çalıştırma

1. **Veritabanı local için:**
    - settings.py içinde bulunan database dict üzerindeki host değeri "db" olmalı      
  
2. **Docker Compose:**
     ```bash
      docker-compose up --build


### Swagger 

1. **Swagger Kullanımı:**
    - http://.../api/swagger üzerinden erişeblirsiniz.  

