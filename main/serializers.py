from rest_framework import serializers

from main.models import Advert, Category, City


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'id',
            'name',
        )


class AdvertListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    city = CitySerializer()

    class Meta:
        model = Advert
        fields = (
            'id',
            'title',
            'description',
            'category',
            'city',
            'views'
        )
