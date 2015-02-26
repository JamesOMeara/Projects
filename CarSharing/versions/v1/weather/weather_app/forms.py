from django import forms

class WeatherDataForm(forms.Form):
    fromPlace = forms.CharField(label="From")
    toPlace    = forms.CharField(label="To")
    date    = forms.DateTimeField(label="Date")
    reg     = forms.CharField(label="reg")

