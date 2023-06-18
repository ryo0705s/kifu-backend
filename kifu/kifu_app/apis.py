from .models import user, donation
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
# from rest_framework.generics import ListCreateAPIView
from .serializers import UserSerializer,DonationSerializer
  
class createDonation(CreateAPIView):
  queryset = donation.objects.all()
  serializer_class = DonationSerializer
  
class getDonation(RetrieveAPIView):
  queryset = donation.objects.all()
  serializer_class = DonationSerializer
  
class getDonationList(ListAPIView):
  queryset = donation.objects.all()
  serializer_class = DonationSerializer
class createUser(CreateAPIView):
  queryset = user.objects.all()
  serializer_class = UserSerializer
  
class getUser(RetrieveAPIView):
  queryset = user.objects.all()
  serializer_class = UserSerializer
  
class getUserList(ListAPIView):
  queryset = user.objects.all()
  serializer_class = UserSerializer
