from rest_framework import serializers
from .models import kifu, donation

class kifuSerializer(serializers.ModelSerializer):
  class Meta:
    model = kifu
    fields = ['id', 'title', 'description', 'mail', 'password', 'donation_amount']
    model = donation
    fields = ['id', 'title', 'description', 'donation_amount']