import os

# Root directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Directory paths
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')
XML_DIR = os.path.join(REPORTS_DIR, 'xml')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')