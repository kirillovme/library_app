from django.urls import path, include
from rest_framework.routers import DefaultRouter
from genre.views import GenreViewSet

router = DefaultRouter()
router.register(r'', GenreViewSet, basename='genre')

urlpatterns = [
    path('', include(router.urls)),
]
