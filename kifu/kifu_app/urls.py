from django.urls import path
from . import apis

urlpatterns = [
  path('api/', apis.api.as_view(), name='api'),
]