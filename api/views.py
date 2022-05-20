from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .models import Photo
from .serializers import PhotoSerializer


class PhotoView(ModelViewSet):
    # IsAuthenticatedOrReadOnly 将允许经过身份验证的用户执行任何请求。仅当请求方法是“安全”方法之一时，才允许未经授权的用户请求
    permission_classes = (IsAuthenticatedOrReadOnly, )

    queryset = Photo.objects.all().order_by('-id')
    serializer_class = PhotoSerializer
