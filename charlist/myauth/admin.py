from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from myauth.models import CharlistUser


class CharlistUserAdmin(UserAdmin):
    pass


admin.site.register(CharlistUser, CharlistUserAdmin)
