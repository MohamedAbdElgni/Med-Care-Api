from django.contrib import admin
from .models import Rating
from appointments.models import Schedule

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'day', 'start_time', 'end_time', 'is_active')
    list_display_links = ('doctor',)  
    list_editable = ('is_active',)  
    list_filter = ('day',) 
admin.site.register(Schedule, ScheduleAdmin)



class RatingAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'user', 'rating', 'comment', 'created_at')
    list_display_links = ('doctor', 'user',)  
    list_editable = ('rating',)  
    list_filter = ('created_at',)  
admin.site.register(Rating, RatingAdmin)

