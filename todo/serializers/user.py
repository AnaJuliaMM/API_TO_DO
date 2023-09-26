from rest_framework import serializers
from ..models.user import UserEntity

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEntity
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}
