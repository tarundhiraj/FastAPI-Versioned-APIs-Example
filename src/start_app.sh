#!/bin/bash
gunicorn -b 0.0.0.0:8080 -k uvicorn.workers.UvicornWorker src.main:app