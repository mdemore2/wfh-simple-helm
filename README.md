# wfh-simple-helm

🎶 everybody's working on the weekend 🎶

## Essential Template Features

- [x] simple deployment
- [x] ports
- [x] secrets
- [x] env vars
- [] volumes
- [] ingresses

### Docker Coommands

- `docker build -t simple-flask ./app/`
- `docker run -p 9001:9001 simple-flask`
- `docker tag simple-flask {yourRepo}/simple-flask`
- `docker push {yourRepo}/simple-flask`

### Helm Commands

- `helm install {my-name} simple-helm`
- `helm uninstall {my-name}`
- `helmfile sync`

### Kubernetes Commands

- `kubectl get deployments`
- `kubectl get services`
- `kubectl get secrets`
- `kubectl describe pods {my-name}`
- `kubectl apply -f secrets.yaml`
- `kubectl exec -it {pod-naame} -- /bin/bash`
