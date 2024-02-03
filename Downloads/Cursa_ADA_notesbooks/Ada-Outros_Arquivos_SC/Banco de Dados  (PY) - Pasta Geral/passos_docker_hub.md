https://hub.docker.com/_/mysql 

No terminal: docker run --name mydb -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=LOJINHA -p 8080:3306 -it --rm  mysql:8.1.0
