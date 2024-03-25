from django.contrib import admin
from .models import UserQuestion

@admin.register(UserQuestion)
class UserQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('question', 'user__username')  # Assuming user has a 'username' field

# Optionally, you can unregister the UserQuestion model if it's already registered elsewhere
# admin.site.unregister(UserQuestion)

