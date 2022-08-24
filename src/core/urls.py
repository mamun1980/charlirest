from django.urls import path, include, re_path
# from django.contrib.auth.models import User
from django.contrib import admin


from rest_framework import routers, permissions
from rest_framework.authtoken.models import Token
# from rest_framework.authtoken.views import obtain_auth_token


# from rest_framework_simplejwt.views import (
#    TokenObtainPairView,
#    TokenRefreshView,
#    TokenVerifyView
# )


# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


from apps.posts.views import *
from apps.charliauth.views import *

# from apps.posts.views import FileUploadView





# schema_view = get_schema_view(
#    openapi.Info(
#       title="Snippets API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )


# # Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register('author', AuthorViewSet)
router.register('department', DepartmentViewSet)
router.register('category', CategoryViewSet)
router.register('movie', MovieViewSet)


urlpatterns = [
   path('admin/', admin.site.urls),

   # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

   path('', include(router.urls)),

   # path('api/get-token/', obtain_auth_token),
   # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

   #  re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   #  path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('silk/', include('silk.urls', namespace='silk'))

   #  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
   #  path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
   #  path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),



]
