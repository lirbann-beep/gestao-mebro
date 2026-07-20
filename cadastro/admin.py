from django.contrib import admin
from .models import Membro
from .views import exportar_membros_excel

@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'whatsapp', 'bairro', 'data_cadastro')
    search_fields = ('nome_completo', 'whatsapp', 'bairro')
    
    actions = ['exportar_para_excel']

    @admin.action(description="Exportar membros selecionados para Excel")
    def exportar_para_excel(self, request, queryset):
        return exportar_membros_excel(request)