from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from .models import Device, DeviceDetail, Booking
from .forms import DeviceForm, DeviceDetailsForm, CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.models import User


def graph_page(request):
  bookings = Booking.objects.all()
  template = loader.get_template('graph-page.html')
  context = {
    'bookings': bookings
  }
  return HttpResponse(template.render(context,request))

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def create_booking(request):
  user = User.objects.all()
  devices = Device.objects.all()
  return render(request, 'create_booking.html', {'devices':devices ,'user': user})

###########################################
###INVENTORY MANAGEMENT VIEWS###
#Manage Inventory
def manage_inventory(request):
  #Get all objects from database
  devices = Device.objects.all()
  device_details = DeviceDetail.objects.all()
  return render(request, 'ManageInventory.html' , {'devices':devices ,'device_details':device_details})

#Get instances of devices to display when table row is clicked on
def get_device_instances(request, device_id):
    #instances related to the specified device clicked on by user
    instances = DeviceDetail.objects.filter(device_id=device_id).values(
        'deviceDetailName', 'deviceSerial', 'deviceRAM', 'deviceCPU', 'deviceGPU')
    instances_list = list(instances)
    # Return instances data as JSON response
    return JsonResponse(instances_list, safe=False)

#Add device view
def add_device(request):
  if request.method == "POST":
    form = DeviceForm(request.POST or None)
    if form.is_valid():
      deviceName = form.cleaned_data['deviceName']
      if Device.objects.filter(deviceName=deviceName).exists():
        #If a device with the same name exists - record is not saved
        return render(request, 'add_device.html',{'form':form})
      form.save()
      return redirect('manage_inventory')
    else:
      return render(request, 'add_device.html')
  else:
    return render(request, 'add_device.html')
  
#Add device details view
def add_devicedetails(request):
  devices = Device.objects.all()
  if request.method == "POST":
    form = DeviceDetailsForm(request.POST or None)
    if form.is_valid():
        device_id = request.POST.get("device")
        if device_id is not None:
            device_id = int(device_id)
            device = Device.objects.get(id=device_id)
            # Increment deviceQuantity attribute when adding to an already existing device
            device.deviceQuantity += 1
            device.save()
            form.save()
            return redirect('manage_inventory')
  else:
    form=DeviceDetailsForm()
  return render(request, 'add_devicedetails.html',{'devices':devices})
  
#Update device view
def update_device(request, device_id):
  device = get_object_or_404(Device,pk=device_id)
  form = DeviceForm(request.POST or None, instance=device)
  if form.is_valid():
    form.save()
    return redirect('manage_inventory')
  else:
    form = DeviceForm(instance=device)
  return render(request,'update_device.html',{'device':device, 'form':form})

#View device instances
def device_instances(request, device_id):
    device = Device.objects.get(id=device_id)
    instances = DeviceDetail.objects.filter(device=device)
    return render(request, 'view_deviceInstance.html', {'device': device, 'instances': instances})

#Update instance view
def update_instance(request, instance_id):
  instance = get_object_or_404(DeviceDetail,pk=instance_id)
  if request.method == "POST":
    instance_form = DeviceDetailsForm(request.POST or None, instance=instance)
    #Remove 'device' field from form
    instance_form.fields.pop('device', None)
    if instance_form.is_valid():
      instance_form.instance.device = instance.device
      instance_form.save()
      device_id = instance.device_id
      return redirect('device_instances', device_id=device_id)
  else:
    instance_form = DeviceDetailsForm(instance=instance)
  return render(request,'update_deviceDetails.html',{'instance':instance, 'instance_form':instance_form})

#Delete a Device
def delete_device(request, device_id):
  device = get_object_or_404(Device,pk=device_id)
  device.delete()
  return redirect('manage_inventory')

#Delete a Device instance
def delete_instance(request, instance_id):
  instance = get_object_or_404(DeviceDetail,pk=instance_id)
  device_id = instance.device_id
  device = get_object_or_404(Device, pk=device_id)
  # Deduct 1 from deviceQuantity when an instance is deleted
  device.deviceQuantity -= 1
  device.save()
  instance.delete()
  if device.deviceQuantity == 0:
    device.delete()
    return redirect('manage_inventory')
  return redirect('device_instances', device_id=device_id)
###########################################

###USER MANAGEMENT VIEWS###
#Manage Users
def manage_users(request):
  #Get all users from database
  users = User.objects.all()
  return render(request,'ManageUsers.html',{'users':users})

#Add user 
def add_user(request):
  if request.method == "POST":
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
      form.save()
      return redirect('manage_users')
  else:
    form = CustomUserCreationForm()
  return render(request, 'add_user.html')
  
#Update user 
def update_user(request, user_id):
  user = get_object_or_404(User,pk=user_id)
  if request.method == "POST":
    user_form = CustomUserChangeForm(request.POST or None, instance=user)
    if user_form.is_valid():
      user_form.save()
      return redirect('manage_users')
    else:
      print(user_form.errors)
  else:
    user_form = CustomUserChangeForm(instance=user)
  return render(request,'update_user.html',{'user':user,'user_form':user_form})
  
#Delete a user
def delete_user(request, user_id):
  user = get_object_or_404(User,pk=user_id)
  user.delete()
  return redirect('manage_users')
###########################################