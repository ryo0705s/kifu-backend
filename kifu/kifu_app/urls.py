from django.urls import path
from . import apis
from django.conf.urls import include

urlpatterns = [
  path('api/createDonation', apis.createDonation.as_view(), name='createDonation'),
  path('api/getDonations', apis.getDonationList.as_view(), name='getDonationList'),
  path('api/getDonations/<int:pk>', apis.getDonation.as_view(), name='getDonation'),
  path('api/createUser', apis.createUser.as_view(), name='createUser'),
  path('api/getUsers', apis.getUserList.as_view(), name='getUserList'),
  path('api/getUsers/<int:pk>', apis.getUser.as_view(), name='getUser'),
  path('api-auth/', include('rest_framework.urls')),
  path('rest-auth/', include('rest_auth.urls')),
  path('rest-auth/registration/', include('rest_auth.registration.urls')),
  path('rest-auth/google/', apis.GoogleLogin.as_view(), name='google_login'),
]