#!/bin/bash

# Activate virtual environment (if applicable)
# source ../../venv/bin/activate

# Install dependencies
pip install -r ../../requirements.txt

# Run pytest and generate XML report
pytest --junitxml=reports/test-results.xml
