from django.urls import include, path
from . import views

urlpatterns = [
    #path('', views.post_list, name='post_list'),#
    path('', views.ktshop_product_info, name='ktshop'),
]