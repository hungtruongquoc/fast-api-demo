#!/bin/bash
uvicorn app.main:app --host :: --port 8080 &
uvicorn app.main:app --host 0.0.0.0 --port 8080