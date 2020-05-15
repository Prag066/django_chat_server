from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Message



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    empty_value_display = '-empty-'
    # fields = ((''),)

# admin.site.register(Profile,ProfileAdmin)
# testing change
# testing change 2
admin.site.register(Message)