- show docker container id: ```docker ps```
- docker-compose down
- show docker volume ``` docker volume  ls ```
- remove volume sql exist with command : ```docker volume rm <name volume>```
- create docker db volume blank with command: ```docker-compose up -d db```
  ```docker-compose up -d <db_name_serivice>``` 
- import sql file with command: ```cat <sqlfile.sql> | docker exec -i <dontainer id> psql -U <username> -d <dbname>```
- for example:   ```cat sixcents-db-2018-11-16.sql | docker exec -i e1a2a1e3ab89 psql -U postgres -d postgres```

- backupdata base: ``` docker exec -t 8d280d9259ed  pg_dumpall -c -U postgres > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql```
