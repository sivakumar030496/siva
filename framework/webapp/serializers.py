from rest_framework import serializers
from .models import employees,Group

class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=employees
       # fields=('firstname','lastname')
        fields='__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields='__all__'
