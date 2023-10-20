from author.views import AuthorViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', AuthorViewSet, basename='author')

urlpatterns = [
    path('', include(router.urls)),
]
