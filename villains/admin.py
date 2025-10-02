from django.contrib import admin
from .models import Vilao

@admin.register(Vilao)
class VilaoAdmin(admin.ModelAdmin):
    list_display = ("codinome", "cidade", "criado_em")
    search_fields = ("codinome", "nome_real", "cidade")
    readonly_fields = ("criado_em",)