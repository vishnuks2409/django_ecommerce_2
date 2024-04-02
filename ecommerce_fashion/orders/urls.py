"""
URL configuration for brokart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from orders import views
app_name='orders'
urlpatterns = [
    path('cart/',views.show_cart,name='cart'),
    path('showorders/',views.show_orders,name='showorders'),

    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('remove_item/<int:pk>/',views.remove_item_from_cart,name='remove_item'),
    path('checkout/',views.checkout_cart,name='checkout')

]
