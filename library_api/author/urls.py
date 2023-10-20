from django.urls import path, include
from rest_framework.routers import DefaultRouter
from author.views import AuthorViewSet

router = DefaultRouter()
router.register(r'', AuthorViewSet, basename='author')

urlpatterns = [
    path('', include(router.urls)),
]
