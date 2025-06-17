import os
import sys
from pathlib import Path

# Vercel serverless function entry point
from mortgauge_project.wsgi import application

# Add the project root to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mortgauge_project.settings')

# Import Django and configure
import django
from django.conf import settings

# Configure Django
django.setup()

# Vercel expects a function named 'handler' or the app itself
def handler(request):
    return application(request)

# Also export the app directly
app = application
