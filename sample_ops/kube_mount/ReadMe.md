# kube mount test

## set volume path


## launch & run pods

```
kubectl apply -f kube.yml
```
## status check

```
kubectl get all 
```


## check

```
kubectl exec -it mount-test ls /usr/share/nginx/html
```

## delete the pod

```
kubectl delete -f kube.yml 
```