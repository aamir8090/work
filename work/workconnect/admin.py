from django.contrib import admin
from .models import RegistrationData


@admin.register(RegistrationData)
class RegistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'message')
