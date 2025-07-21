FROM python:3.12-slim-bookworm
# Copy the uv binary from the official uv image for fast dependency management
COPY --from=ghcr.io/astral-sh/uv:0.8.0 /uv /uvx /bin/

WORKDIR /app

COPY . /app

# Install dependencies using the lock file
# uv default group is dev, ignore it for production env
RUN uv sync --frozen --no-cache --no-dev

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]