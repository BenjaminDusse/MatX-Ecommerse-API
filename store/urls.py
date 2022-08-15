from django.urls import path
from store import views
from rest_framework import routers



router = routers.DefaultRouter()
router.register('products', views.ProductListViewSet)

urlpatterns = router.urls

