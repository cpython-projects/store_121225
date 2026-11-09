from rest_framework import viewsets
from store.models import Supplier
from store.serializers.product import SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
