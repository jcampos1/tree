from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    children = serializers.StringRelatedField(many=True)

    class Meta:
        model = Account
        fields = '__all__'

    @staticmethod
    def validate_parent(value):
        # If the node wants to be saved as root
        if value is None:
            root_count = Account.objects.filter(parent=None).count()
            if root_count > 0:
                raise serializers.ValidationError('There is already a root.')

        return value

    @staticmethod
    def update(instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.parent = validated_data.get('parent', instance.parent)

        if instance.parent is not None:
            if instance.parent.id == instance.id:
                raise serializers.ValidationError('Father and son can not be the same.')

        instance.save()
        return instance
