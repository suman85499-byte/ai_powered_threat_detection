import os
import sys

os.environ["VERCEL"] = "1"

# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Import Flask application directly
from web.app import app

# Explicit Vercel application entry point
application = app
