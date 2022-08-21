from django.urls import path
from store import views
from rest_framework import routers


# urlpatterns = [
#     path("users/", views.UsersListView.as_view(), name="users"),

# ]

urlpatterns = [
    
]
router = routers.DefaultRouter()
router.register('products', views.ProductListViewSet, 'products')
router.register('users', views.UserViewSet, 'users')

urlpatterns += router.urls
