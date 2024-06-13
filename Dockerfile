FROM python:3.12.3-slim

RUN pip install --no-cache-dir --break-system-packages poetry

ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY todo_app/ todo_app/
COPY tests/ tests/

RUN poetry install --no-root

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
