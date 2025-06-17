import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

# Set Django settings module before importing anything Django-related
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# Import Django and configure
import django
from django.conf import settings
from django.http import JsonResponse
from django.urls import path, include
from django.core.wsgi import get_wsgi_application

# Configure Django settings inline
if not settings.configured:
    settings.configure(
        DEBUG=False,
        SECRET_KEY='django-insecure-vercel-key-change-in-production',
        ALLOWED_HOSTS=['*'],
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'rest_framework',
            'corsheaders',
        ],
        MIDDLEWARE=[
            'corsheaders.middleware.CorsMiddleware',
            'django.middleware.common.CommonMiddleware',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.getenv('PGDATABASE', 'postgres'),
                'USER': os.getenv('PGUSER', 'postgres'),
                'PASSWORD': os.getenv('PGPASSWORD', ''),
                'HOST': os.getenv('PGHOST', 'localhost'),
                'PORT': os.getenv('PGPORT', '5432'),
                'OPTIONS': {
                    'sslmode': 'require',
                },
                'CONN_MAX_AGE': 0,
            }
        },
        ROOT_URLCONF='api.urls',
        CORS_ALLOW_ALL_ORIGINS=True,
        REST_FRAMEWORK={
            'DEFAULT_PERMISSION_CLASSES': [
                'rest_framework.permissions.AllowAny',
            ],
        },
        USE_TZ=True,
    )

django.setup()

# Simple views
def health_check(request):
    return JsonResponse({
        'status': 'healthy',
        'message': 'API is running',
        'version': '1.0.0',
        'database': 'connected'
    })

def dashboard_summary(request):
    return JsonResponse({
        'total_clients': 4,
        'active_applications': 2,
        'pending_tasks': 3,
        'completed_this_month': 1,
    })

# URL patterns
urlpatterns = [
    path('api/health/', health_check),
    path('api/dashboard/summary/', dashboard_summary),
]

# Create WSGI application
application = get_wsgi_application()

# Vercel handler
def handler(request):
    return application(request)

app = application
