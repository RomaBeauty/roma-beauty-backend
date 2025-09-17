from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views.purchase import PurchaseViewSet  # importação absoluta

router = DefaultRouter()
router.register(r'purchases', PurchaseViewSet, basename='purchase')

urlpatterns = [
    path('api/', include(router.urls)),
]
