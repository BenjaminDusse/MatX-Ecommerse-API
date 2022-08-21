from store.filters import ProductFilter
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from users.models import User
from users.serializers import UserSerializer
from store.models import Product
from store.serializers import ProductSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser


# new leads: users
# this week sales
# inventory status
# orders to deliver

# top selling products
# filter this month, last month


# active users
# transactions count


# pending products
# need set profile model for user O2O

# chart-dashboard: transaction sources
# campaigns today, yesterday, before yesterday

class UserViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet
                  ):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    


class ProductListViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_class = ProductFilter

