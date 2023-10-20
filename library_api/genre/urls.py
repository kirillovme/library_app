from django.urls import include, path
from genre.views import GenreViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', GenreViewSet, basename='genre')

urlpatterns = [
    path('', include(router.urls)),
]
