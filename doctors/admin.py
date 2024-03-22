from django.contrib import admin
from .models import Doctor
from django.contrib.auth.models import Group
from django.db import models
from users.models import User

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'degree', 'area', 'fees')
    list_display_links = ('user',)
    list_editable = ('fees', 'degree')
    list_filter = ('area',)

admin.site.register(Doctor, DoctorAdmin)

