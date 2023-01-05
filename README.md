# Server_And_Cloud_Project

## Run this project:

* minikube start;
* minikube dashboard &
* kubectl proxy --address='0.0.0.0' --disable-filter=true &
* kubectl apply -f ./db_deploy.yaml && kubectl apply -f ./flask_pot.yaml

## Manually Backup the Mysql database:
bash backup.sql
