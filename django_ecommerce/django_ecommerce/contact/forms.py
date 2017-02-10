from django.forms import ModelForm
from .models import ContactForm
from django import forms


class ContactView(ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'topic', 'message']
