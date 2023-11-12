from django.contrib import admin
from app.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=["name","password","email"]

admin.site.register(User)
