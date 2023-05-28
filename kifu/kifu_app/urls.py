from django.urls import path
from . import apis

urlpatterns = [
  path('api/<int:pk>', apis.api.as_view(), name='api'),
]