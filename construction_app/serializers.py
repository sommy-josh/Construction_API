from rest_framework import serializers
from .models import Contact, GetQUote,Home

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Home
        fields=['image']
