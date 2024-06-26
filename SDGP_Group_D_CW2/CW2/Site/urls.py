from django.urls import path, include
from . import views

urlpatterns = [
    path('graph_page/', views.graph_page, name='graph_page'),
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('manage_select', views.manage_select, name='manage_select'),
    path('manage_inventory/', views.manage_inventory, name='manage_inventory'),
    path('manage_inventory/add_device', views.add_device, name='add_device'),
    path('manage_inventory/add_devicedetails', views.add_devicedetails, name='add_devicedetails'),
    path('manage_inventory/update_device/<int:device_id>/', views.update_device, name='update_device'),
    path('manage_inventory/update_instance/<int:instance_id>/', views.update_instance, name='update_instance'),
    path('device/<int:device_id>/instances', views.device_instances, name='device_instances'),
    path('manage_inventory/delete_device/<int:device_id>/', views.delete_device, name='delete_device'),
    path('instances/delete_instance/<int:instance_id>/', views.delete_instance, name='delete_instance'),
    path('get_device_instances/<int:device_id>/', views.get_device_instances, name='get_device_instances'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('manage_users/add_user', views.add_user, name='add_user'),
    path('manage_users/update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('manage_users/delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('create_booking/', views.create_booking, name='create_booking'),
    path('graph_page/<int:booking_id>/edit/', views.edit_booking, name='edit_booking'),
    path('graph_page/<int:booking_id>/delete/', views.delete_booking, name='delete_booking'),
    path('confirm_booking', views.confirm_booking, name='confirm_booking'),
    path('user_bookingSelect', views.user_bookingSelect, name='user_bookingSelect'),
]
