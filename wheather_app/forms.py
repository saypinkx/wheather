from django import forms
class WheatherForm(forms.Form):
    city = forms.CharField(label='Город')