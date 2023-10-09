"""Onlineshopbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_nested import routers
from mainapp.views import Catagoryviewset,chapa_payment,my_webhook_view,ProfileViewSet,SubCatagoryviewset,allproductViewset,Newsviewset,NewProductViewset,Productviewset,Top_viewset,OrderItemViewset,OrderViewsSet
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
router = routers.DefaultRouter()
router.register(r'catagory', Catagoryviewset)

router.register(r'News', Newsviewset)
router.register(r'Allproduct', allproductViewset)
router.register('customer',ProfileViewSet,basename='customer')


router.register(r'order',OrderViewsSet)
router.register(r'newproducts',NewProductViewset,basename="newproducts")
router.register(r'topsell',Top_viewset,basename="Topsells")
subcatagory_router=routers.NestedDefaultRouter(router,r'catagory',lookup='catagory')
subcatagory_router.register(r'subcatagory',SubCatagoryviewset,basename='subcatagory')
product_router=routers.NestedDefaultRouter(router,r'catagory',lookup='catagory')
product_router.register(r'product',Productviewset,basename='product')
order_router = routers.NestedSimpleRouter(router, r'order', lookup='order')
order_router.register(r'orderitems', OrderItemViewset, basename='Orderitems')

urlpatterns = [
    path('admin/', admin.site.urls),
     path(r'', include(router.urls)),
     path(r'', include(order_router.urls)),
     path(r'',include(product_router.urls)),
       path(r'',include(subcatagory_router.urls)),
         path('auth/', include('djoser.urls')),
     path('auth/', include('djoser.urls.jwt')),
      path('chapa/',chapa_payment)
    ,path('webhook/',my_webhook_view),
     path('chapa-webhook/', include('django_chapa.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

