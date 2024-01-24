#!/bin/bash

# Activate virtual environment
source ../../venv/bin/activate

# Install dependencies
pip install -r ../../requirements.txt

# Run pytest and generate XML report
pytest --junitxml=reports/test-results.xml
