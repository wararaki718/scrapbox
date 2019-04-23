# BUILD & RUN

## local run

### run
```
$ cd app
$ sh run.sh
```

### check api
```
$ curl localhost:8000
```

## docker build & run

### build
```
$ docker-compose build
```

### run
```
$ docker-compose up
```

### check api
```
$ curl localhost:8000
```

## k8s deploy & run

### kubectl deploy
```
$ kubectl apply -f kube.yml
```

### set loadbalancer
```
$ kubectl expose deployment fastapi --type=LoadBalancer --name=my-service
```

### check api (via loadbalancer)
```
$ curl localhost:8000
```
