from rest_framework import serializers
from .models import user, donation

class kifuSerializer(serializers.ModelSerializer):
  class Meta:
    model = user
    fields = ['id', 'mail', 'password', 'total_donation_amounts']
    model = donation
    fields = ['id', 'user','donation_amount']