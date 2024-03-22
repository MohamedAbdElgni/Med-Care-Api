from django.contrib import admin
from .models import User
admin.site.site_header = "Med_Care"
admin.site.site_title = "Med_Care"

class UserAdmin(admin.ModelAdmin):
    list_display = ('gender','is_patient','is_doctor','phone','img','age','address','city')
    list_display_links = ('img',)  
    list_editable = ('gender',) 
    list_filter = ('gender',) 

admin.site.register(User, UserAdmin)
