from django.urls import path
from . import views

urlpatterns = [
    path('graph_page/', views.Site, name='Site'),
]
