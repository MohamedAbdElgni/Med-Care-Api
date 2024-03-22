from django.contrib import admin
from .models import Schedule
from .models import Appointment
from django.contrib.auth.models import Group



class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor','schedule','user','create_at','is_accepted' )
    list_display_links = ('doctor','schedule','user')  
    list_editable = ('is_accepted',)  
    list_filter = ('doctor__user',) 

admin.site.register(Appointment, AppointmentAdmin)

