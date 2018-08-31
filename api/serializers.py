from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    children = serializers.StringRelatedField(many=True)

    class Meta:
        model = Account
        fields = '__all__'
