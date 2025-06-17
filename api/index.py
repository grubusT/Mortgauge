import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

# Set Django settings module before importing anything Django-related
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mortgauge_project.settings')

# Import Django and configure
import django
from django.conf import settings

try:
    django.setup()
except Exception as e:
    print(f"Django setup error: {e}")

# Import the WSGI application
from mortgauge_project.wsgi import application

# Vercel handler
def handler(request):
    return application(request)

# Export the app
app = application
