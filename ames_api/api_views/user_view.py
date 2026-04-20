from rest_framework import viewsets, permissions
from ames_api.models import CustomUser
from ames_api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    


    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            # Solo l'utente stesso o un admin può modificare/cancellare
            return [permissions.IsAuthenticated()] 
        return [permissions.AllowAny()]

