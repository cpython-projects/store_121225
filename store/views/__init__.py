from .categories import CategoryViewSet
from .product import (ProductRetrieveUpdateDestroyAPIViewSet, ProductListCreateViewSet,
                      ProductDetailListCreateViewSet, ProductDetailRetrieveUpdateDeleteView)
from .supplier import SupplierViewSet
from .address import AddressViewSet
from .customer import CustomerListCreateView, CustomerDetailUpdateDeleteView