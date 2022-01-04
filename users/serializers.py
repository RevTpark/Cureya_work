from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password


class RegisterUserSerializers(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

