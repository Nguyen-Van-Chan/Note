## công nghệ sử dụng 
- python https://www.codecademy.com/catalog/language/python
- django https://docs.djangoproject.com/en/4.0/ 
- restapi  https://www.django-rest-framework.org/tutorial/1-serialization/
- docker https://docs.docker.com/get-started/
- celery https://docs.celeryproject.org/en/stable/
- postgresql https://www.postgresql.org/docs/


## TẠO ENV 
Sử dụng conda
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
theo cách thông thường 
https://docs.python.org/3/library/venv.html
- tạo project sử dụng django-admin strat project 

### Một số lệnh trong manage.py 
- startproject tạo project 
- shell chạy thử lệnh 
- startapp tạo app 
- runserver chạy dự án 
- makemigrations tạo ra file mô tả, lưu lại lịch sử thay đổi trên cơ sở dữ liệu 
- migrate thực thi những lệnh do makemigrations tạo ra rồi apply nó vào trong database thật 
-

### Tổ chức thư mục 

1. Gợi ý 
- https://github.com/sonnhfit/django_base
- https://github.com/saleor/saleor
- https://github.com/MicroPyramid/Django-CRM
- https://github.com/creativetimofficial/black-dashboard-django

2. default 
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

4.

5. unit test https://pytest-django.readthedocs.io/en/latest/

#### lưu trữ media 
- https://boto3.amazonaws.com/v1/documentation/api/latest/index.html


### docker service 
- nginx webserver, proxy, cân bằng tải
- redis cơ sở dữ liệu trên ram cache. OTP tồn tại 60s sử dụng redis 
- db: 
    - backup + restore https://github.com/sonnhfit/mynote/blob/master/load_sql_docker.MD

- celery: lập lịch, bất đồng bộ, task chạy ẩn 


Trong docker mỗi service thì là một cái container có thể nói một cách dễ  hiểu là một cái máy ảo, mình phải cài rất nhiều thứ linh tinh ví dụ phần mềm, thư viện, env, ... nó định nghĩa trong file `docker-compose.yaml` và file `Dockerfile`


- build: đi settup những gì mình đã định nghĩa ở trên 

    - `docker-compose build`
    - `docker-compose build --no-cache`
- chạy dự án 
    - `docker-compose up` chạy dự án 
    - `docker-compose up -d` để chạy ẩn trang web khi tắt terminal 
    - `docker ps` hiển thị những dịch vụ đang chạy 
- xoá container, image, volume 
    - docker rm <container id>
    
    ### tao admin user 
    ```
    docker-compose run web python manage.py createsuperuser
    ```
    
    ### quy trình viết một API 
    - viết model 
    
    ```
    
    class Order(models.Model):
        email = models.CharField(max_length=255)
        address = models.CharField(max_length=255)

    ```
    - makemigration 
    ```
    docker-compose run web python manage.py makemigrations
    ```
    - migrate để tạo ra bảng ở db 
    ```
    docker-compose run web python manage.py migrate
    ```
    - nếu thích thì thêm admin để quản lí hay xem nhanh 
    - viết một cái view (có thể tuỳ từng task vụ mà anh sẽ cần gọi đến cái ultil, hoặc task celery, background task)
        - định nghĩa tham số serializer của django rest framework 
        - get 
        - post 
        - put 
        - delete 
    - liên kết cái view đó với một url 
    
    
    
    ## update data với API của hệ thống thứ 3 vào trong database của mình 
    
    ### Thông qua webhook 
        - Viết một API để insert data vào trong database 
        - Cài đặt API vào trong webhook của trang web bên thứ 3(ví dụ: shoppee) thường là để link của cái API ở bước trên vào 
    
    
    ### cứ 1 time nhất định thì vào trang đó lấy dữ liệu hoặc gọi API lấy dữ liệu 
        - Viết một task của celery gọi API hoặc vào trang web của bên thứ 3 lấy dữ liệu -> thêm vào database 

    
    
    
    
    
    



