# sidecar pattern check

## deploy & running
```
kubectl apply -f kube.yml
```

## get status
```
kubectl get all
```

## check
```
kubectl exec pod-with-sidecar -c sidecar-container -it bash
cd /usr/share/nginx/html
tail -f app.txt 
```

## delete containers
```
kubectl delete -f kube.yml
```