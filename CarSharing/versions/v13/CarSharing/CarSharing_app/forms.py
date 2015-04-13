from django import forms

class CarSharingDataForm(forms.Form):
    fromPlace = forms.CharField(label="From")
    toPlace    = forms.CharField(label="To")
    time    = forms.DateTimeField(label="Date")
    reg     = forms.CharField(label="Car Reg")
    seats_free = forms.IntegerField(label="Seats Free")


BOOLEAN_CHOICES = (('Male','Male'), ('Female','Female'))
CLIENT_CHOICES = (('Driver','Driver'), ('Passanger','Passanger'))
DEVIATE_CHOICE = (('0km','No'),('5','5km'), ('10','10km'), ('15+','15km +'))

class details_ClientForm(forms.Form):
  firstname = forms.CharField(label="First Name:")
  lastname = forms.CharField(label="Last Name:")
  email = forms.CharField(label="Email:")
  age = forms.IntegerField(label="Age:")
  phone = forms.IntegerField(label="Contact Number:")
  gender = forms.ChoiceField(choices = BOOLEAN_CHOICES)
  client_is = forms.ChoiceField(choices = CLIENT_CHOICES) 
  home = forms.CharField(label="Home Address:")


class routeForm(forms.Form):
    journey_name = forms.CharField(label="Route Name:")
    from_place = forms.CharField(label="From:")
    to_place    = forms.CharField(label="To:")
    time    = forms.DateTimeField(label="Date:")
    price = forms.IntegerField(label="Price overall:")
    seats_free = forms.IntegerField(label="Seats Available:")
    car_desc= forms.CharField(label="Car Description:")
    deviate = forms.ChoiceField(choices = DEVIATE_CHOICE)


class messagesForm(forms.Form):
  messageTo = forms.CharField(label="To:")
  driverMessage = forms.CharField(label="Message:")
  #time    = forms.DateTimeField(label="Date:")
  

    
#add details in for users car
class drivers_carForm(forms.Form):
  car_reg = forms.CharField(label="Car Reg:")
  car_desc = forms.CharField(label="Car Description:")
  seats_free = forms.CharField(label="Num Seats:")

  
  