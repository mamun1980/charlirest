from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from .views import *

post_router = routers.DefaultRouter()
post_router.register('author', AuthorViewSet)
post_router.register('department', DepartmentViewSet)
post_router.register('category', CategoryViewSet)
post_router.register('movie', MovieViewSet)





# urlpatterns = router.urls
