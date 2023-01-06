# Server_And_Cloud_Project

## Generate SSL keys:
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365

## Run this project:

* minikube start;
* minikube dashboard &
* kubectl proxy --address='0.0.0.0' --disable-filter=true &
* kubectl apply -f ./db_deploy.yaml && kubectl apply -f ./flask_pot.yaml

## Manually Backup the Mysql database:
bash backup.sql
