from rest_framework import serializers
from .models import user, donation

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = user
    fields = ['id', 'mail', 'password', 'total_donation_amounts']
class DonationSerializer(serializers.ModelSerializer):
  class Meta:
    model = donation
    fields = ['id', 'user','donation_amount']