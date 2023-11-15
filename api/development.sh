#!/bin/bash

# Run the server with debug mode
uvicorn heygpt:application --host 0.0.0.0 --port 23450 \
  --reload --log-level debug
