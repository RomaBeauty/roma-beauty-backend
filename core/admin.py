"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models
from core.models.purchase import Purchase
from core.models.category import Category  # importa o model Category
from core.models.tipo import Tipo  # importa o model Tipo
from core.models.colecao import Colecao  # importa o model Colecao
from core.models.produto import Produto  # importa o model Produto
from core.models.sacola import ItemSacola
from core.models.favorito import Favorito


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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)
    list_filter = ('nome',)


@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'categoria')
    search_fields = ('nome',)
    list_filter = ('categoria',)


@admin.register(Colecao)
class ColecaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)
    filter_horizontal = ('tipos',)  # permite selecionar vários tipos


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'colecao', 'tipo', 'category', 'preco')
    search_fields = ('nome',)
    list_filter = ('colecao', 'tipo', 'category')
    readonly_fields = ('descricao_colecao', 'imagem_mostruario_colecao')

    fieldsets = (
        ('Informações do Produto', {
            'fields': ('nome', 'colecao', 'tipo', 'category', 'preco', 'imagem_produto', 'imagem_amostra')
        }),
        ('Informações da Coleção', {
            'fields': ('descricao_colecao', 'imagem_mostruario_colecao')
        }),
    )
@admin.register(ItemSacola)
class ItemSacolaAdmin(admin.ModelAdmin):
    list_display = ('user', 'produto', 'quantidade', 'adicionado_em')
    list_filter = ('user', 'produto')
    search_fields = ('user__email', 'produto__nome')
    readonly_fields = ('adicionado_em',)
    fieldsets = (
        ('Informações da Sacola', {
            'fields': ('user', 'produto', 'quantidade', 'adicionado_em')
        }),
    )


@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('user', 'produto', 'adicionado_em')
    list_filter = ('user', 'produto')
    search_fields = ('user__email', 'produto__nome')
    readonly_fields = ('adicionado_em',)
    fieldsets = (
        ('Favoritos', {
            'fields': ('user', 'produto', 'adicionado_em')
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
