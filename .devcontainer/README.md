# Dev Container for k8s-draft-demo

This project includes a [devcontainer](https://containers.dev/) configuration for reproducible development with Docker, Minikube, Helm, and Python.

## Features
- Python 3.11
- Docker-in-Docker
- Minikube, kubectl, and Helm preinstalled
- VS Code extensions for Python, Docker, and Kubernetes

## Usage
1. Open this folder in VS Code and install the "Dev Containers" extension if prompted.
2. Reopen in container when prompted (or use the Command Palette: "Dev Containers: Reopen in Container").
3. The container will install Python dependencies automatically.
4. You can use Docker, Minikube, and Helm inside the container as described in the main README.

> **Note:** If you want to run Minikube inside the devcontainer, you may need to use the `none` driver or Docker driver, and run as root. See [Minikube docs](https://minikube.sigs.k8s.io/docs/drivers/) for details.
