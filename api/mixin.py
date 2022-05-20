from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class AuthenticatedModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )