from .models import kifu
from rest_framework.generics import ListCreateAPIView
from .serializers import kifuSerializer

class api(ListCreateAPIView):
  queryset = kifu.objects.all()
  serializer_class = kifuSerializer 