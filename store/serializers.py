from rest_framework.serializers import ModelSerializer
from store.models import *

from store.models import Promotion


class PromotionSerializer(ModelSerializer):
    class Meta:
        model = Promotion
        fields = ('description', 'discount', )


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'image', 'unit_price', 'inventory')


class ProductSerializer(ModelSerializer):
    promotions = PromotionSerializer(many=True)

    class Meta:
        model = Product
        fields = ('title', 'slug', 'description', 'unit_price',
                  'inventory', 'last_update', 'collection', 'promotions')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['collection'] = instance.collection.title
        return representation
