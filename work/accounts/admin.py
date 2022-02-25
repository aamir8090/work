from django.contrib import admin
from .models import *
from .import models
# Register your models here.

class accountsAdminArea(admin.AdminSite):
    site_header='Accounts Area'
accounts_side=accountsAdminArea(name='accountsAdmin')
accounts_side.register(models.Profile)
admin.site.register(Profile)

