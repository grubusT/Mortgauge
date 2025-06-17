"""
URL configuration for mortgauge_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from broker_operations import views

schema_view = get_schema_view(
    openapi.Info(
        title="Mortgage Broker API",
        default_version='v1',
        description="API for Mortgage Broker Operations Assistant",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'applications', views.ApplicationViewSet)
router.register(r'documents', views.DocumentViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'reminders', views.ReminderViewSet)
router.register(r'scripts', views.InterviewScriptViewSet)
router.register(r'script-sections', views.ScriptSectionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/health/', views.health_check, name='health_check'),
    path('api/dashboard/summary/', views.dashboard_summary, name='dashboard_summary'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
