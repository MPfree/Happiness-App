from rest_framework import serializers
from .generic_models import Item

class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    price = serializers.IntegerField()
    rarity = serializers.CharField(max_length = 100)

    def create(self, validated_data):
        return Item(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.rarity = validated_data.get('rarity', instance.rarity)
        return instance