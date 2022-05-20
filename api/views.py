from rest_framework.viewsets import ModelViewSet
from .models import Photo
from .serializers import PhotoSerializer
from .mixin import AuthenticatedModelViewSet
from rest_framework.permissions import IsAuthenticated


class PhotoView(ModelViewSet):
    # permission_classes = (IsAuthenticated, )

    queryset = Photo.objects.all().order_by('-id')
    serializer_class = PhotoSerializer
