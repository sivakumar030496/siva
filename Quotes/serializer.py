from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class QuoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)
