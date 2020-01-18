from django.urls import path,include
#Django Resteframework
from rest_framework.routers import DefaultRouter 


from .views import ProductList


router = DefaultRouter()
router.register(r'products',ProductList,basename="_products")


urlpatterns = [
    path('',include(router.urls)),
]