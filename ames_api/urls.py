
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views.user_view import UserViewSet
from .api_views.corsa_view import CorsaViewSet
from .api_views.sample_view import SampleViewSet
from .views import import_local_csv

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user_view')
router.register(r'corsas', CorsaViewSet, basename='corsa_view')
router.register(r'samples', SampleViewSet, basename='sample_view')

urlpatterns = [
    path('', include(router.urls)),
    path('csv/', import_local_csv), 
]
