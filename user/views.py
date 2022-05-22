from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .seriazlizers import UserSerializer
from .models import User


class UserView(ModelViewSet):
    permission_classes = (IsAuthenticated, )

    queryset = User.objects.all()
    serializer_class = UserSerializer
