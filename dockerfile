FROM ghcr.io/astral-sh/uv:python3.10-bookworm-slim

WORKDIR /app

# Install zstd and tar for extracting .tar.zst files (as required by the data section)
RUN apt-get update && apt-get install -y zstd tar && rm -rf /var/lib/apt/lists/*

ENV VIRTUAL_ENV=/app/.venv
RUN uv venv $VIRTUAL_ENV


ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY pyproject.toml .

RUN uv pip install 'stable-worldmodel[train,env]'  && \ 
uv pip install .


COPY . .

VOLUME ["/app/files"]
ENV STABLEWM_HOME=/app/files
ENV HYDRA_FULL_ERROR=1


CMD ["python", "main.py"]