clone o repositorio
para o REDIS
```
sudo service redis stop
```
pare o POSTGRES
```
sudo service postgresql stop
```

```
docker-compose build
```
verifique o container
```
docker ps
```
suba o projeto

```
docker-compose up
```
(ou docker exec -it <container_id>)
