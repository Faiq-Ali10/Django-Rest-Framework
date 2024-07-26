# extractor/urls.py
from django.urls import path
from .views import DocumentViewSet, upload_file
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    path('api/upload/', upload_file, name='upload_file'),
] + router.urls

