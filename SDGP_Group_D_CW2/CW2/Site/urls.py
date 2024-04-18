from django.urls import path
from . import views

urlpatterns = [
    path('graph_page/', views.graph_page, name='graph_page'),
    path('', views.index, name='index'),
    path('manage_inventory/', views.manage_inventory, name='manage_inventory'),
    path('manage_users/', views.manage_users, name='manage_users'),
]
