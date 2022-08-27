
Cài đặt docker và docker compose ở link dưới
- install docker : https://docs.docker.com/install/linux/docker-ce/ubuntu/
- install docker-compose: https://docs.docker.com/compose/install/#install-compose
- set permission for docker user: sudo usermod -aG docker $USER
- you should reboot system
- create pyenv virtualenv [python-version] [version-name]
- pyenv local [env name] #set local env for folder with pyenv 
- add docker with pycharm
- buid docker: docker-compose up --build

## run redis docker compose
```
docker-compose run redis redis-server
```


To delete all containers including its volumes use,

docker rm -vf $(docker ps -a -q)
To delete all the images,

docker rmi -f $(docker images -a -q)
remove all docker volume
```
docker volume rm $(docker volume ls -q)
```
Note docker copy file from folder to volume data
```
docker container create --name dummy -v myvolume:/root hello-world
docker cp c:\myfolder\myfile.txt dummy:/root/myfile.txt
docker rm dummy
```
### một số lệnh docker hay dùng
- Để build một dự  án docker sử dụng compose  
```
docker-compose build 
```
- Để chạy một dự án đã build 
```
docker-compose up
```

###  một số lệnh linux  hay dùng 
-  hiển thị file trong thư mục 
```
ls 
```
- xoá 1 thư mục   
```
rm -rf tenthumuc 
```
- Chuyển thư mục làm việc ở terminal  
```
cd tenthumuc
```
- Trở về thư mục cha 
```
cd ../
```
