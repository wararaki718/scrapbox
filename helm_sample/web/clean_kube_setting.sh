#!/bin/bash

kubectl delete deploy web
kubectl delete deploy redis
kubectl delete service web
kubectl delete service redis
echo "DONE"
