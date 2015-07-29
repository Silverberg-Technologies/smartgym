from django.contrib import admin
from django.contrib.auth.models import User
from users.models import Groupsession
from users.models import SmartGymUser

# Register your models here.
class GroupsessionAdmin(admin.ModelAdmin):
    list_display = ('name','coach', 'date_time')

class SmartGymUserAdmin(admin.ModelAdmin):
    list_display = ('is_moderator', 'is_instructor')

admin.site.register(Groupsession, GroupsessionAdmin)
admin.site.unregister(User)
admin.site.register(User, SmartGymUserAdmin)
