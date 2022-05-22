from . import views
from django.urls import path


urlpatterns = [
    path('photo/', views.PhotoView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('photo/<int:pk>', views.PhotoView.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
        'put': 'update',
        'patch': 'perform_update'
    }))
]
