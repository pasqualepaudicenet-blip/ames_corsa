import hashlib
from rest_framework import viewsets, permissions
from ames_api.models import CustomUser
from ames_api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.core.cache import cache
from django.db.models import Q

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    


    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            # Solo l'utente stesso o un admin può modificare/cancellare
            return [permissions.IsAuthenticated()] 
        return [permissions.AllowAny()]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.request.query_params.get('username', None)
        email = self.request.query_params.get('email', None)

        filters = Q()
        if username:
            filters &= Q(username__icontains=username)
        if email:
            filters &= Q(email__icontains=email)
        if filters:
            queryset = queryset.filter(filters)
        return queryset 

    def list(self, request, *args, **kwargs):
        params_string = str(sorted(request.query_params.items()))
        user_part = f"user_{request.user.id}" if request.user.is_authenticated else "anon"
        cache_key = f"user_list_{user_part}_{hashlib.md5(params_string.encode()).hexdigest()}"

        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        # usa il flow DRF corretto
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = self.get_paginated_response(serializer.data).data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data

        cache.set(cache_key, data, timeout=60 * 5)

        return Response(data)
