from django.contrib import admin
from .models import TgUser
# Register your models here.


@admin.register(TgUser)
class TgUserAdmin(admin.ModelAdmin):
    pass
