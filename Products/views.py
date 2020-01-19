# django 
# restframework
from rest_framework import viewsets,mixins
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# serializers
from Products.serializers import ProductsSerializer, CategoriesSerializer
# models
from Products.models import Categories, Products
#permissions
from rest_framework.settings import api_settings


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000

class RangeFilterBackend(filters.BaseFilterBackend):
 
    def filter_queryset(self, request, queryset, view):
        try:
            params = request.query_params.get('price_range').split('-')
            if not params:
                return queryset
            return queryset.filter(price__range=(params[0],params[1]))
        except:
            return queryset

        
        

class ProductList(
               mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               mixins.ListModelMixin,
               viewsets.GenericViewSet):

    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, RangeFilterBackend]
    filterset_fields = ['quantity','available']
    search_fields = ['name', 'code']
    ordering_fields = ['price', 'quantity',]
    

class CategoriesView(
               mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               mixins.ListModelMixin,
               viewsets.GenericViewSet):

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    pagination_class = LargeResultsSetPagination

