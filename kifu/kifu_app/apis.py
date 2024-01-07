from .models import user, donation
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
# from rest_framework.generics import ListCreateAPIView
from .serializers import UserSerializer,DonationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.utils.translation import gettext_lazy as _
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_auth.views import LoginView
from rest_framework.response import Response
from rest_framework import status

class CustomLoginView(LoginView):
    print("user")
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = self.user
        # ユーザー情報を含めたレスポンスを返す
        data = {
            'user': {
                'id': user.id,
                'username': user.username,
                # 他のユーザー情報を追加
            },
            # 'access_token': response.data['access_token'],
            'refresh_token': response.data['refresh_token'],
        }
        return Response(data, status=status.HTTP_200_OK)
class LoginView(LoginView):
  def post(self, request):
   username = request.data.get('email')  # フロントエンドのリクエストに合わせて修正
   password = request.data.get('password')
   user = authenticate(username=username, password=password)
   print(username, "refresh ")
   if user is not None:
     refresh = RefreshToken.for_user(user)
     return Response({
       'access_token': str(refresh.access_token),
       'refresh_token': str(refresh),
      })
   else:
    return Response(status=status.HTTP_401_UNAUTHORIZED)
# class TokenObtainView(APIView):
#     authentication_classes = (JSONWebTokenAuthentication)

#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = authenticate(username=username, password=password)
#         if user is not None:
#             token = JWTSerializer().from_user(user)

#             return Response({'token': token})
#         else:
#             return Response(status=status.HTTP_401_UNAUTHORIZED)
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

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://127.0.0.1/callback'
    client_class = OAuth2Client
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)