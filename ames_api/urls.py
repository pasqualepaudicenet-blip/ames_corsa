
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views.user_view import UserViewSet
from .api_views.corsa_view import CorsaViewSet, CorsaSampleCreateView
from .api_views.sample_view import SampleViewSet
from .views import import_local_csv
#from .api_views.get_corsa_data_view import CorsaSampleCreateView

corsa_list_view = CorsaSampleCreateView.as_view()

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user_view')
router.register(r'corsas', CorsaViewSet, basename='corsa_view')
router.register(r'samples', SampleViewSet, basename='sample_view')

urlpatterns = [
    path('', include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('csv/', import_local_csv), 
    path('get-data/', corsa_list_view, name="corsa_list_view"), 
]
