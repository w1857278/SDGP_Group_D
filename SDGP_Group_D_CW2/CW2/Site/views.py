from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .models import Device, DeviceDetail
from .forms import DeviceForm, DeviceDetailsForm

def graph_page(request):
  template = loader.get_template('graph-page.html')
  return HttpResponse(template.render())
def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
#Manage Inventory
def manage_inventory(request):
  #Get all objects from database
  devices = Device.objects.all()
  device_details = DeviceDetail.objects.all()
  template = loader.get_template('ManageInventory.html')
  context = {
    'devices': devices,
    'device_details': device_details,
  }
  return HttpResponse(template.render(context,request))
#Manage Users
def manage_users(request):
  template = loader.get_template('ManageUsers.html')
  return HttpResponse(template.render())