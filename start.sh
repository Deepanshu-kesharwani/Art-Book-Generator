#!/bin/bash

# Run FastAPI in background (internal use)
uvicorn main:app --host 0.0.0.0 --port 8000 &

# Run Streamlit on HF-required port
streamlit run frontend/app.py \
  --server.port 7860 \
  --server.address 0.0.0.0