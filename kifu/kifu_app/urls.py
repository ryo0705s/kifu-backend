from django.urls import path
from . import apis

urlpatterns = [
  path('api/<int:pk>', apis.api.as_view(), name='api'),
  path('api/create', apis.create.as_view(), name='create'),
  path('api/get', apis.getList.as_view(), name='getList'),
  path('api/get/<int:pk>', apis.get.as_view(), name='get'),
]