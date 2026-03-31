docker build -t lewm:latest -f dockerfile . && docker run  --name lewm_container \
                                                           --gpus all \
                                                           -v /mnt/data/lewm/files:/app/files \
                                                           --env-file .env \
                                                           lewm:latest