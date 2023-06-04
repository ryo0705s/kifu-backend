from django.urls import path
from . import apis

urlpatterns = [
  path('api/<int:pk>', apis.api.as_view(), name='api'),
  path('create', apis.create.as_view(), name='create'),
]