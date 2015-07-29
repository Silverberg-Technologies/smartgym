from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from users.models import Groupsession
from users.models import SmartGymUser

# Register your models here.
class GroupsessionAdmin(admin.ModelAdmin):
    list_display = ('name','coach', 'date_time')

class SmartGymInline(admin.StackedInline):
    model = SmartGymUser
    can_delete = False
    verbose_name_plural = 'SmartGym users'

class SmartGymUserAdmin(UserAdmin):
    inlines = (SmartGymInline, )

admin.site.register(Groupsession, GroupsessionAdmin)
admin.site.unregister(User)
admin.site.register(User, SmartGymUserAdmin)
