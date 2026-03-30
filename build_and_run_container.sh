docker build -t lewm:latest -f Dockerfile . && \
docker run  --name lewm_container --gpus all \
-v /mnt/data/lewm/files:/app/files \
lewm:latest