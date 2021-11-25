from rest_framework import serializers
from .models import CardItem

class CardItemSerializers(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=254)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False,default=1)

    class Meta:
        model = CardItem
        fields = ('__all__')