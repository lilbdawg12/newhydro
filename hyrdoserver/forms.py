from django.db import models
from django.db.models import Model
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    contact = forms.CharField(widget=forms.Textarea)
        