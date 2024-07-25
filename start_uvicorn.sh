#!/bin/bash
# Ensure the directory exists
mkdir -p /etc/datadog-agent

# Create a minimal datadog.yaml configuration file dynamically
cat << EOF > /etc/datadog-agent/datadog.yaml
api_key: ${DD_API_KEY}
site: ${DD_SITE}
EOF

datadog-agent run &
uvicorn app.main:app --host :: --port 8080 &
uvicorn app.main:app --host 0.0.0.0 --port 8080