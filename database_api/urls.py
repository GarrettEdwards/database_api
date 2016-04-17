"""database_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_api import views


router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)
router.register(r'ticket', views.CustomerViewSet)
router.register(r'event', views.EventViewSet)
router.register(r'seating', views.SeatingViewSet)
router.register(r'payment', views.PaymentViewSet)
router.register(r'card', views.CardViewSet)
router.register(r'check', views.CheckViewSet)
router.register(r'cash', views.CashViewSet)
router.register(r'vendor', views.VendorViewSet)
router.register(r'space', views.SpaceViewSet)
router.register(r'staff', views.StaffViewSet)
router.register(r'position', views.PositionViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
