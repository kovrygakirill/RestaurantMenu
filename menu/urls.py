from django.urls import path
from rest_framework.routers import DefaultRouter
from RestaurantMenu.settings import DEBUG

from .views import DishViewSet

if DEBUG:
    router = DefaultRouter()
    router.register(r'dish', DishViewSet, basename='dish')

    urlpatterns = router.urls
else:
    urlpatterns = [
        path(r'dish/', DishViewSet.as_view({'get': 'list', })),
    ]
