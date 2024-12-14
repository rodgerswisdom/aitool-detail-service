#!/usr/bin/env bash

set -o errexit
#source venv/bin/activate
python -m gunicorn tool_service.asgi:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
