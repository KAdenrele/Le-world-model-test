FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim
WORKDIR /app
COPY pyproject.toml .
RUN uv pip install --system .
VOLUME /Users/akomolafe/Documents/le-wm/stable-wm:/app/stable-wm
ENV STABLEWM_HOME=/app/stable-wm
COPY download_tars.py .
COPY eval.py .
COPY train.py .
COPY utils.py .
COPY jepa.py .
COPY module.py .
COPY config/ .
VOLUME ["/app/files"]

CMD ["sh", "-c", "uv run download_tars.py && uv run train.py data=pusht"]