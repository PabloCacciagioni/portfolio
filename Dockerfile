FROM python:3.12.3-slim

EXPOSE 8000

RUN pip install --no-cache-dir --break-system-packages poetry

WORKDIR /app

COPY pyproject.toml ./
COPY poetry.lock ./
COPY todo_app/ todo_app/

RUN poetry install

CMD ["poetry", "run", "uvicorn", "todo_app.api:app", "--host", "0.0.0.0", "--port", "8000"]
