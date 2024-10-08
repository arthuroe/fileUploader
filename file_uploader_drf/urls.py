from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fileupload.views import FileUploadViewSet

router = DefaultRouter()
router.register(r'uploads', FileUploadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
