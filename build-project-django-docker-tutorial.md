Bật termial ở máy rồi thực hiện các bước sau
### 1. Tạo 1 thư mục mới bằng lệnh sau 
```
mkdir tenthumuc  
```
trong đó ```tenthumuc``` la tên thư mục của bạn 

### 2. di chuyển thư mục làm việc working dir vào trong thư mục vừa tạo 

```
cd tenthumuc 
```

### 3. tạo virtual env với pyenv lưu ý cần cài đặt pyenv và sử dụng pyenv để install python 3.6.6 trước 

```
pyenv virtualenv 3.6.6 newenv 

```
### 4. active env bằng lệnh sau 
``` pyenv local newenv ```

### 5. cài đặt django bằng lệnh 

``` pip install django ```

sau đó tạo requaiment file để cấu hình các package và thư viện dùng cho dự án như sau 


``` pip freeze > requirements.txt```

### 6. tạo project django mới bằng lệnh sau 

```
django-admin startproject yourproject .
```
lưu ý là lệnh trên có đáu "." 

### 7. tạo 1 file 
``` docker-compose.yml ```
với nội dung như sau 


```shell 
version: '3.6'

services:
  db:
    image: postgres:10
    ports:
      - "5432:5432"
    environment:
      POSTGRES_PASSWORD: rootapp123
    volumes:
      - postgres_data:/var/lib/postgresql/data/
  web:
    build: .
    command: bash -c "python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
volumes:
  postgres_data:

```
### 8. Tạo 1 file 
```Dockerfile```
Với nội dung như sau 

```shell 
FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt-get update && apt-get install -y gettext libgettextpo-dev
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

```
### 9. Mở website trên trình duyệt nếu thấy trang default của django màu xanh lá là oke 
địa chỉ ở 
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)


hoặc 

[http://0.0.0.0:8000/](http://0.0.0.0:8000/)


