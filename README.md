# Kubernetes Guestbook App

A simple guestbook application built with Flask and MySQL and deployed on Kubernetes.

I made this project to practice the main Kubernetes concepts I have learned, including Deployments, Services, ConfigMaps, Secrets, Persistent Volumes, Namespaces and Ingress.

## What this project uses

- Python Flask
- MySQL
- Docker
- Kubernetes
- Minikube
- ConfigMap
- Secret
- PersistentVolumeClaim
- Service
- Ingress

## Project structure

```text
kubernetes-guestbook-app/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── templates/
│   └── static/
│
├── k8s/
│   ├── namespace.yml
│   ├── mysql-configmap.yml
│   ├── mysql-secret.yml
│   ├── mysql.yml
│   ├── flask-configmap.yml
│   ├── flask-secret.yml
│   ├── flask.yml
│   └── ingress.yml
│
└── .gitignore
```

## How it works

The Flask application handles the guestbook page and stores messages in MySQL.

Kubernetes runs the Flask application with 3 replicas.

MySQL uses a PersistentVolumeClaim so the database data is stored separately from the MySQL container.

ConfigMaps are used for normal configuration values and Secrets are used for the database passwords.

The Flask application connects to MySQL through the Kubernetes Service called `mysql-service`.

The Flask application is exposed internally through `flask-service`.

Ingress is used to access the application through:

```text
/guestbook
```

The Ingress rewrites this path to `/` before sending the request to Flask.

## Kubernetes concepts practiced

### Namespace
Created a separate namespace called `guestbook-dev` for the project.

### Deployment
Used a Deployment for Flask with 3 replicas and MySQL with 1 replica.

### Service
Used ClusterIP Services for communication between Flask and MySQL.

### ConfigMap
Used ConfigMaps for database host, port, database name and username.

### Secret
Used Secrets for database passwords.

### Persistent storage
Used a PersistentVolumeClaim for MySQL data.

### Ingress
Used NGINX Ingress for host and path-based routing.

## Docker

The Flask application uses a multi-stage Docker build.

The first stage builds the Python dependencies and the second stage runs the application using a smaller production image.

The container also runs as a non-root user.

## Running the project

This project was tested locally using Minikube.

The Docker image needs to be available to Minikube before creating the Flask Pods.

After the Kubernetes resources are created, check the Pods, Services and Ingress in the `guestbook-dev` namespace.

## What I learned

While building this project I practiced:

- Connecting multiple Kubernetes resources together
- Using labels and selectors
- Connecting Flask to MySQL using a Kubernetes Service
- Using ConfigMaps and Secrets
- Using persistent storage for MySQL
- Running multiple Flask replicas
- Setting up NGINX Ingress
- Debugging Kubernetes networking
- Understanding the difference between Service ports and container ports
- Debugging application errors separately from Kubernetes errors

## Note

This is a learning project built locally with Minikube. It is not intended as a production deployment.
