FROM python:3.11-slim AS base

WORKDIR /app_dir

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY ./pyproject.toml .
COPY ./README.md .
COPY ./src ./src/
COPY ./model ./model/

RUN pip install -e .


FROM base AS backend
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
