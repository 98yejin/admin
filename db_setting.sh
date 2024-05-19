docker pull postgres:latest
docker run -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=1234 -e TZ=Asia/Seoul -d postgres:latest
