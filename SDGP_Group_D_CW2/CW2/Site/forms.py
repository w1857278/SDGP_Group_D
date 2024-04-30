from django import forms
from .models import Device, DeviceDetail, Booking
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['deviceName', 'deviceType', 'deviceQuantity', 'deviceAudit', 'deviceLocation', 'deviceStatus', 'deviceComments']

class DeviceDetailsForm(forms.ModelForm):
    device = forms.ModelChoiceField(queryset=Device.objects.all(), to_field_name='id')
    class Meta:
        model = DeviceDetail
        fields = ['device', 'deviceDetailName', 'deviceSerial', 'deviceRAM', 'deviceCPU','deviceGPU']

class BookingForm(forms.ModelForm):
    userID = forms.ModelChoiceField(queryset=User.objects.all(), to_field_name='id')
    deviceID = forms.ModelChoiceField(queryset=Device.objects.all(), to_field_name='id')
    dueDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Booking
        fields = ['userID', 'deviceID', 'bookingType', 'dueDate']

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    is_staff = forms.BooleanField(required=False)
    
    class Meta:
        model = User
        fields = ('username', 'is_staff', 'first_name', 'last_name', 'email', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    is_staff = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('username', 'is_staff', 'first_name', 'last_name', 'email')
     
class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    is_staff = forms.BooleanField(required=False)
    
    class Meta:
        model = User
        fields = ('username', 'is_staff', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
class LoginForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    is_staff = forms.BooleanField(required=False)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')        