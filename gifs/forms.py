from django import forms
from django.core.validators import validate_email

class GifForm(forms.Form):
    title = forms.CharField(max_length=200)
    url = forms.URLField()
    uploader_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control-lg'}))
    field_order = ['title','uploader_name','url']