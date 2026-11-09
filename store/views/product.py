from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from store.models import Product, ProductDetail
from store.serializers.product import (ProductSerializer, ProductCreateUpdateSerializer, ProductDetailSerializer,
                                       ProductDetailCreateUpdateSerializer)
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ProductListCreateViewSet(ListCreateAPIView):
    queryset = Product.objects.all()
    authentication_classes = [TokenAuthentication] #[BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        return ProductCreateUpdateSerializer


class ProductRetrieveUpdateDestroyAPIViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        return ProductCreateUpdateSerializer


class ProductDetailListCreateViewSet(ListCreateAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductDetailSerializer
        return ProductDetailCreateUpdateSerializer


class ProductDetailRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductDetailSerializer
        return ProductDetailCreateUpdateSerializer


