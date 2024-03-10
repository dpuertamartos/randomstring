1. `docker build -t flask-app .`
2. `username=insert_your_docker_registry_username`
3. `docker tag flask-app $username/flask-app:latest`
`docker push $username/flask-app:latest`
4 `k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2`
5 `kubecetl apply -f .`
6 Check in browser accesing `localhost:8081` that you get random string generation!
