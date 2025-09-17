"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models
from core.models.purchase import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'email', 'telefone', 'cidade', 'estado', 'created_at']
    list_filter = ['estado', 'cidade', 'created_at']
    search_fields = ['nome', 'sobrenome', 'email', 'telefone']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'sobrenome', 'email', 'telefone')
        }),
        ('Endereço', {
            'fields': ('cep', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ['id']
    list_display = ['email', 'name']
    readonly_fields = ['last_login']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name', 'passage_id')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
        (_('Groups'), {'fields': ('groups',)}),
        (_('User Permissions'), {'fields': ('user_permissions',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'name',
                'is_active', 'is_staff', 'is_superuser'
            ),
        }),
    )


admin.site.register(models.User, UserAdmin)
