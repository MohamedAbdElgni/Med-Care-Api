from django.contrib import admin
from .models import *




class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    list_filter = ('created_at',)  
admin.site.register(ContactMessage, ContactAdmin)

