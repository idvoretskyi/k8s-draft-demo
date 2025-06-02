# k8s-draft-demo: Local Kubernetes Demo

This project demonstrates running a Python app on your local Kubernetes cluster (e.g., Minikube) using Helm and Draft-generated configs.

## Prerequisites
- [Docker](https://www.docker.com/)
- [Minikube](https://minikube.sigs.k8s.io/docs/)
- [Helm](https://helm.sh/)
- Python app files: `app.py` and `requirements.txt`

## Steps

1. **Start Minikube**
   ```sh
   minikube start
   ```

2. **Build the Docker image inside Minikube**
   ```sh
   eval $(minikube docker-env)
   docker build -t k8s-draft-demo:latest .
   ```

3. **Deploy with Helm**
   ```sh
   helm install k8s-draft-demo ./charts
   ```

4. **Access the App**
   - If using `service.type=LoadBalancer` (default):
     ```sh
     minikube tunnel
     # In another terminal:
     kubectl get svc -n default
     # Find the EXTERNAL-IP and open in browser
     ```
   - Or, port-forward:
     ```sh
     kubectl port-forward svc/k8s-draft-demo 8080:80
     # Visit http://localhost:8080
     ```

5. **Cleanup**
   ```sh
   helm uninstall k8s-draft-demo
   minikube stop
   ```

## Notes
- Edit `charts/values.yaml` to customize environment variables or ports.
- Make sure your `app.py` listens on port 80 (or update `containerPort`).
- If you change the image name or tag, update `values.yaml` accordingly.
