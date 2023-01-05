minikube start;
minikube dashboard &
sleep 2
kubectl proxy --address='0.0.0.0' --disable-filter=true &