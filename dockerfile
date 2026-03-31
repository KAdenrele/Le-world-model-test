FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim
WORKDIR /app

# Install zstd and tar for extracting .tar.zst files
RUN apt-get update && apt-get install -y zstd tar && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .
RUN uv pip install --system .
ENV STABLEWM_HOME=/app/stable-wm
COPY download_tars.py .
COPY . .
VOLUME ["/app/files"]

CMD ["uv", "run", "main.py"]