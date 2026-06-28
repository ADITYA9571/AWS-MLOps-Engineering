# Docker Commands Cheat Sheet

## Build an Image

```bash
docker build -t my-app .
```

---

## List Images

```bash
docker images
```

---

## Run a Container

```bash
docker run -p 8000:8000 my-app
```

---

## Run in Detached Mode

```bash
docker run -d -p 8000:8000 my-app
```

---

## Running Containers

```bash
docker ps
```

---

## All Containers

```bash
docker ps -a
```

---

## Stop a Container

```bash
docker stop <container_id>
```

---

## Remove a Container

```bash
docker rm <container_id>
```

---

## Remove an Image

```bash
docker rmi <image_id>
```

---

## View Logs

```bash
docker logs <container_id>
```

---

## Execute Commands Inside Container

```bash
docker exec -it <container_id> bash
```

---

## Docker Compose

Start services

```bash
docker compose up
```

Run in background

```bash
docker compose up -d
```

Stop services

```bash
docker compose down
```

Rebuild images

```bash
docker compose up --build
```

---

## Clean Up

Remove stopped containers

```bash
docker container prune
```

Remove unused images

```bash
docker image prune
```

Remove everything unused

```bash
docker system prune
```