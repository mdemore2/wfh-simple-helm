# wfh-simple-helm

🎶 everybody's working on the weekend 🎶

## Docker Coommands

- `docker build -t simple-flask ./app/`
- `docker run -p 9001:9001 simple-flask`
- `docker tag simple-flask {yourRepo}/simple-flask`
- `docker push {yourRepo}/simple-flask`

## Helm Commands

- `helm install {my-name} simple-helm`
- `helm uninstall {my-name}`
- `helmfile sync`
- `helm install {my-name} simple-helm -f secrets.yaml`

## Kubernetes Commands

- `kubectl get deployments`
- `kubectl get services`
- `kubectl describe pods {my-name}`
- `kubectl apply -f secrets.yaml`
