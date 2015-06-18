from django.contrib import admin
from users.models import Groupsession

# Register your models here.
class GroupsessionAdmin(admin.ModelAdmin):
    list_display = ('name','coach', 'date_time')

admin.site.register(Groupsession, GroupsessionAdmin)
