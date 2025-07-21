FROM python:3.12-slim-bookworm
# Copy the uv binary from the official uv image for fast dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY . /app

# Install dependencies using the lock file
RUN uv sync --frozen --no-cache

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]