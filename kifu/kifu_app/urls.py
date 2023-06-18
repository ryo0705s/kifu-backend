from django.urls import path
from . import apis

urlpatterns = [
  path('api/createDonation', apis.createDonation.as_view(), name='createDonation'),
  path('api/getDonations', apis.getDonationList.as_view(), name='getDonationList'),
  path('api/getDonations/<int:pk>', apis.getDonation.as_view(), name='getDonation'),
  path('api/createUser', apis.createUser.as_view(), name='createUser'),
  path('api/getUsers', apis.getUserList.as_view(), name='getUserList'),
  path('api/getUsers/<int:pk>', apis.getUser.as_view(), name='getUser'),
]