from django import forms

class Biodataform(forms.Form):
    name = forms.CharField(max_length=10)
    age = forms.IntegerField()
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)