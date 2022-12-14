from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.http import request
from rest_framework import serializers
from virtualenv.create import creator

from advertisements.models import Advertisement

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name']

class AdvertisementSerializer(serializers.ModelSerializer):

    creator = UserSerializer(
        read_only=True)
    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'description', 'creator',
                  'status', 'created_at']
        read_only_fields  = ['creator']


    def create(self, validated_data):
         validated_data["creator"] = self.context["request"].user
         return super().create(validated_data)
         return(data)

        #"""Метод для валидации. Вызывается при создании и обновлении."""
        # TODO: добавьте требуемую валидацию


