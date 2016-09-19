from django.contrib import admin
from .models import ContactForm


class ContactFormAdmin(admin.ModelAdmin):
    class Meta:
        model = ContactForm

admin.site.register(ContactForm, ContactFormAdmin)
