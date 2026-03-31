FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim
WORKDIR /app

# Install zstd and tar for extracting .tar.zst files
RUN apt-get update && apt-get install -y zstd tar && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .
RUN uv pip install --system .
COPY . .
VOLUME ["/app/files"]
ENV STABLEWM_HOME=/app/files
ENV HYDRA_FULL_ERROR=1
CMD ["uv", "run", "main.py"]