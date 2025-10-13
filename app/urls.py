from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import UserViewSet
from core.views.purchase import PurchaseViewSet   # 👈 importa o PurchaseViewSet
from core.views.category import CategoryViewSet   # 👈 importa o CategoryViewSet
from core.views.tipo import TipoViewSet   # 👈 importa o TipoViewSet
from core.views.colecao import ColecaoViewSet   # 👈 importa o ColecaoViewSet
from core.views.produto import ProdutoViewSet  #importa o ProdutoViewSet
from core.views.sacola import ItemSacolaViewSet 
from core.views.favorito import FavoritoViewSet


router = DefaultRouter()
router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'purchases', PurchaseViewSet, basename='purchases')
router.register(r'categories', CategoryViewSet, basename='categories')  # 👈 adiciona aqui
router.register(r'tipos', TipoViewSet, basename='tipos')
router.register(r'colecoes', ColecaoViewSet, basename='colecoes')
router.register(r'produtos', ProdutoViewSet, basename='produtos')
router.register(r'sacola', ItemSacolaViewSet, basename='sacola')
router.register(r'favoritos', FavoritoViewSet, basename='favoritos')

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
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)