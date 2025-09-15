FROM python:3.13-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_NO_INTERCTION=1 \
    PYTHONPATH=/app

WORKDIR /app


COPY ./ ./

RUN pip install -U pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root

EXPOSE 5001
ENTRYPOINT [ "sh","./api/entrypoint.sh" ]