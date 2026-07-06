#!/bin/bash
set -e

echo "🚀 Starting the Jupyter Notebook & Streamlit Ambient..."

# streamlit run academic/src/app.py --server.port=8501 --server.address=0.0.0.0 &
exec jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''