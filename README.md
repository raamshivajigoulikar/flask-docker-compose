# Flask Celery Docker Compose

## Initial build

```
git clone https://github.com/seanfcarroll/flask-docker-compose.git
cp ~/apps/secrets.py flask-docker-compose/flask-celery/
docker-compose build
docker-compose up -d
```

## Get status and logs
```
docker-compose ps
docker ps
docker logs 7b7ff37ed2d5
```

## Rebuild a specfic container
```
docker-compose ps
docker-compose stop web
docker-compose rm web
docker-compose up -d
```


### Start, stop, delete
```
stop all containers:
docker kill $(docker ps -q) &&  docker rm $(docker ps -a -q) && docker rmi $(docker images -q)

remove all containers
docker rm $(docker ps -a -q)

remove all docker images
docker rmi $(docker images -q)
```

### Shell into container
```
sudo docker exec -i -t 665b4a1e17b6 /bin/bash
```

## Smoke Test

[Home page](http://localhost:5000/)

## Monitor

[Home page](http://localhost:5555/)

## Scaling

```
docker-compose scale worker=5
```
This will create 4 more containers each running a worker. http://your-dockermachine-ip:5555 should now show 5 workers waiting for some jobs!


## Development Only

The ```flask-celery/secrets.py``` file allows access to the Rails server on OS X using the special address:

```docker.for.mac.localhost```
