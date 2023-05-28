from rest_framework import serializers
from .models import kifu

class kifuSerializer(serializers.ModelSerializer):
  class Meta:
    model = kifu
    fields = ['id', 'title', 'description', 'mail', 'password', 'donation_amount']