from django import forms

class CarSharingDataForm(forms.Form):
    fromPlace = forms.CharField(label="From")
    toPlace    = forms.CharField(label="To")
    time    = forms.DateTimeField(label="Date")
    reg     = forms.CharField(label="Car Reg")
    seats_free = forms.IntegerField(label="Seats Free")

class details_driverForm(forms.Form):
  driver_id = forms.CharField(label="ID:")
  firstname = forms.CharField(label="First Name:")
  lastname = forms.CharField(label="Last Name:")
  password = forms.CharField(label="Password:")
  email = forms.CharField(label="Email:")
  age = forms.IntegerField(label="Age:")
  phone = forms.IntegerField(label="Contact Number:")
  gender = forms.CharField(label="Gender")
  home = forms.CharField(label="Home Address:")
  car_reg = forms.CharField(label="Car Reg")
  car_desc = forms.CharField(label="Car Description")
  seats_free = forms.CharField(label="Number of seats in car")