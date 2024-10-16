from rest_framework import serializers
from Shops.models import shop

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop
        fields = '__all__'
        read_only_fields = ['id', 'distance']