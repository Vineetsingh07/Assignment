from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', 'company_name', 'city', 'state')
    list_display_links = ('id', 'first_name')



admin.site.register(User,UserAdmin)
