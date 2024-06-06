FROM python:3.12.3-slim

RUN apt-get update && apt-get install -y curl

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY todo_app/ todo_app/
COPY tests/ tests/

RUN poetry install --no-root

COPY . .

CMD [ "poetry", "run", "python", "-m", "unittest", "discover", "-s", "tests" ]