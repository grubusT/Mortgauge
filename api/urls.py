from django.urls import path
from . import index

urlpatterns = [
    path('api/health/', index.health_check),
    path('api/dashboard/summary/', index.dashboard_summary),
]
