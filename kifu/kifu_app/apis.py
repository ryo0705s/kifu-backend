from .models import user, donation
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
# from rest_framework.generics import ListCreateAPIView
from .serializers import UserSerializer,DonationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
  
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
  filter_backends = [DjangoFilterBackend,SearchFilter]
  filterset_fields = ['mail','password']
  search_fields = ['mail','password']
  # def get_queryset(self):
  #   queryset = user.objects.all()
  #   usermail = self.request.query_params.get('mail', None)
  #   userpassword = self.request.query_params.get('password', None)
  #   if usermail is not None:
  #     queryset = queryset.filter(mail=usermail)
  #   if userpassword is not None:
  #     queryset = queryset.filter(password=userpassword)
  #   return queryset
