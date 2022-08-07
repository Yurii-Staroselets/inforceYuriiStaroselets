from .models import Menu
from rest_framework import viewsets, permissions, generics
from .serializers import MenuSerializer
from knox.models import AuthToken
from accounts.serializers import UserSerializer


# Get User API
class MenuViewSet(generics.RetrieveAPIView, viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.AllowAny,
    ]
    serializer_class = UserSerializer
    serializer_class = MenuSerializer

    def get_object(self):
        return self.request.user




