docker build
docker push localhost:5000/sample-web

kompose convert
kompose up
kubectl describe service web