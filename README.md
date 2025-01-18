# wfh-simple-helm

🎶 Everybody's working on the weekend 🎶

## Docker Instructions

- `docker build -t simple-flask ./app/`
- `docker run -p 9001:9001 simple-flask`
- `docker tag simple-flask {yourRepo}/simple-flask`
- `docker push {yourRepo}/simple-flask`

## Helm Instructions

- `helm install {my-name} simple-helm`
