from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.unregister(Group)
admin.site.site_header='Django admin - test page'
