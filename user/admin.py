from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from . import models

class UserAdmin(BaseUserAdmin):
    ordering = ['-id']
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_display = ['email', 'first_name', 'last_name', 'phone_number']
    fieldsets = (
        (None, {'fields': ('email', 'password')}), 
        (_('Personal Info'), {'fields': ('avatar','first_name', 'last_name','phone_number', 'date_of_birth', 'referal_code', 'gender', 'location',)}), 
        (
            _('Permissions'),
            {
                'fields': ('role', 'is_phone_number_verified', 'is_email_verified', 'is_staff','is_active', 'is_superuser')
            }
        ), 
        (_('important dates'), {'fields': ('last_login', 'date_joined',)})
    )

    add_fieldsets = (
        (None, {'classes': ('wide', ), 'fields': ('email', 'password1')}),
    )

admin.site.register(models.User, UserAdmin)