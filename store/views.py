from rest_framework import viewsets
from store.models import Product
from store.serializers import ProductSerializer


class ProductListViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




