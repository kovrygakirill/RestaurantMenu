from rest_framework import serializers

from .models import FoodCategory, Food


class FoodSerializer(serializers.ModelSerializer):
    topping = serializers.StringRelatedField(many=True)

    class Meta:
        model = Food
        fields = [
            'name', 'description', 'price',
            'is_special', 'is_vegan', 'topping',
        ]


class DishSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = [
            'id', 'name', 'foods',
        ]
