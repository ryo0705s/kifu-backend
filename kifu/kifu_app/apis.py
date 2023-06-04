from .models import kifu, donation
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView
# from rest_framework.generics import ListCreateAPIView
from .serializers import kifuSerializer

class api(RetrieveAPIView):
  queryset = kifu.objects.all()
  serializer_class = kifuSerializer 
class create(CreateAPIView):
  queryset = donation.objects.all()
  serializer_class = kifuSerializer