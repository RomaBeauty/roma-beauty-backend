from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models.purchase import Purchase
from ..serializers.purchase import PurchaseSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response({
            'message': 'Compra criada com sucesso!',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            'count': queryset.count(),
            'results': serializer.data
        })

    @action(detail=False, methods=['get'])
    def by_city(self, request):
        city = request.query_params.get('cidade')
        if city:
            purchases = self.get_queryset().filter(cidade__icontains=city)
            serializer = self.get_serializer(purchases, many=True)
            return Response(serializer.data)

        return Response(
            {'error': 'Parâmetro cidade é obrigatório'},
            status=status.HTTP_400_BAD_REQUEST
        )
