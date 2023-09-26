from rest_framework import serializers
from ..models.user import UserEntity

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEntity
        fields = "__all__"
        #Definimos o campo password como somente de escrita para que não seja vazado pelo método
        extra_kwargs = {'password': {'write_only': True}}

    