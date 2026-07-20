from django.db import models
from django.core.validators import RegexValidator

class Membro(models.Model):
    METODOS_PAGAMENTO = [
        ('mpesa', 'M-Pesa'),
        ('term_mola', 'e-Mola'),
        ('mkesh', 'mKesh'),
        ('transferencia', 'Transferência Bancária'),
        ('tesoureiro', 'Direto ao Tesoureiro'),
    ]

    nome_completo = models.CharField(max_length=255, verbose_name="Nome Completo")
    
    # Este validador aceita apenas números (0-9) e exige entre 7 e 15 dígitos (padrão internacional)
    validador_telefone = RegexValidator(
        regex=r'^\d{7,15}$',
        message="O número de WhatsApp deve conter apenas números, sem letras ou espaços, e ter entre 7 e 15 dígitos."
    )
    
    whatsapp = models.CharField(
        max_length=20, 
        validators=[validador_telefone], 
        verbose_name="Número de WhatsApp"
    )
    
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    bairro = models.CharField(max_length=100, verbose_name="Bairro/Zona de Residência")
    
    # Princípios e Conduta
    compromisso_sigilo = models.BooleanField(verbose_name="Compromisso com o sigilo absoluto")
    nao_discriminacao = models.BooleanField(verbose_name="Compromisso de não-discriminação")
    proibicao_comercial = models.BooleanField(verbose_name="Ciente da proibição de fins comerciais/políticos")
    
    # Gestão Financeira
    disponibilidade_contribuicao = models.BooleanField(verbose_name="Disponibilidade para a contribuição de 100 MZN")
    metodo_preferencial = models.CharField(max_length=20, choices=METODOS_PAGAMENTO, default='mpesa', verbose_name="Método Preferencial de Pagamento")
    
    # Integração, Motivação e Atividade
    motivacao = models.TextField(verbose_name="O que te motivou a entrar no grupo?")
    membro_ativo = models.BooleanField(verbose_name="Estás disposto a ser um membro ativo do grupo?")
    doar_conhecimento = models.BooleanField(verbose_name="Estás disposto a doar teu conhecimento para fazer crescer o grupo?")
    habilidades = models.TextField(verbose_name="Quais habilidades você reconhece ter que podem ajudar o grupo a crescer?")
    
    aceitou_regras = models.BooleanField(verbose_name="Aceitou o Regulamento?")
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_completo