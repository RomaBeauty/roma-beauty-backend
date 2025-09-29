from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import UserViewSet
from core.views.purchase import PurchaseViewSet   # 👈 importa o PurchaseViewSet
from core.views.category import CategoryViewSet   # 👈 importa o CategoryViewSet
from core.views.tipo import TipoViewSet   # 👈 importa o TipoViewSet

router = DefaultRouter()
router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'purchases', PurchaseViewSet, basename='purchases')
router.register(r'categories', CategoryViewSet, basename='categories')  # 👈 adiciona aqui
router.register(r'tipos', TipoViewSet, basename='tipos')

urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
]
