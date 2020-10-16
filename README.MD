1) clone o repositorio

2) pause o REDIS
```
sudo service redis stop
```
3) pare o POSTGRES
```
sudo service postgresql stop
```
4) vamos buildar o projeto com o docker
```
docker-compose build
```
5) verifique o container
```
docker ps
```

6)suba o projeto

```
docker-compose up
```
(ou docker exec -it <container_id>)
