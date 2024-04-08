from django.urls import path
from . import views

urlpatterns = [
    path('graph_page/', views.graph_page, name='graph_page'),
    path('', views.index, name='index')
]
