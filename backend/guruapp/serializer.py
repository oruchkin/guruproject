from rest_framework import serializers
from .models import (Shop, City, Street)
from rest_framework import serializers

class City_serializer(serializers.ModelSerializer):
    """ Сериалайзер для городов """
    class Meta:
        model = City
        exclude = ["created", "modified"]


class Street_serializer(serializers.ModelSerializer):
    """ Сериалайзер для улиц """
    class Meta:
        model = Street
        fields = ['id','title']


class Shop_serializer(serializers.ModelSerializer):
    """ Сериалайзер для магазинов """
    class Meta:
        model = Shop
        exclude = ["created", "modified"]


# class Shop_validator_Serializer(serializers.Serializer):
#     #email = serializers.EmailField()
#     content = serializers.CharField(max_length=200)
#     created = serializers.TimeField()