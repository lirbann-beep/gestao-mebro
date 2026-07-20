from django import forms
from .models import Membro

class MembroForm(forms.ModelForm):
    # Forçamos as caixas a exigir o clique (aceitação) obrigatório no formulário
    compromisso_sigilo = forms.BooleanField(required=True, label="Compromisso com o sigilo absoluto")
    nao_discriminacao = forms.BooleanField(required=True, label="Compromisso de não-discriminação")
    proibicao_comercial = forms.BooleanField(required=True, label="Ciente da proibição de fins comerciais/políticos")
    disponibilidade_contribuicao = forms.BooleanField(required=True, label="Disponibilidade para a contribuição de 100 MZN")
    membro_ativo = forms.BooleanField(required=True, label="Estás disposto a ser um membro ativo do grupo?")
    doar_conhecimento = forms.BooleanField(required=True, label="Estás disposto a doar teu conhecimento para fazer crescer o grupo?")
    aceitou_regras = forms.BooleanField(required=True, label="Aceitou o Regulamento?")

    class Meta:
        model = Membro
        fields = [
            'nome_completo', 
            'whatsapp', 
            'data_nascimento', 
            'bairro', 
            'compromisso_sigilo', 
            'nao_discriminacao', 
            'proibicao_comercial', 
            'disponibilidade_contribuicao', 
            'metodo_preferencial', 
            'motivacao', 
            'membro_ativo', 
            'doar_conhecimento', 
            'habilidades', 
            'aceitou_regras'
        ]
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'required': 'required'}),
            'nome_completo': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'whatsapp': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ex: 258841234567 (Apenas números, inclua o código do país)', 
                'required': 'required'
            }),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'motivacao': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'required': 'required'}),
            'habilidades': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'required': 'required'}),
            'metodo_preferencial': forms.Select(attrs={'class': 'form-control'}),
        }