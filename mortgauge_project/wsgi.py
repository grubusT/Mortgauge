"""
WSGI config for mortgauge_project project.
"""

import os
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mortgauge_project.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
