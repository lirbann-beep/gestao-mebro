import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Membro
from .forms import MembroForm

def cadastro_membro(request):
    if request.method == 'POST':
        form = MembroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sucesso/')
    else:
        form = MembroForm()
    return render(request, 'cadastro/index.html', {'form': form})

def sucesso(request):
    return render(request, 'cadastro/sucesso.html')

def exportar_membros_excel(request):
    membros = Membro.objects.all().values()
    df = pd.DataFrame(list(membros))

    # Limpeza de datas para evitar erros no Excel
    for col in df.select_dtypes(['datetime', 'datetimetz']).columns:
        df[col] = df[col].dt.tz_localize(None)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="lista_membros.xlsx"'
    df.to_excel(response, index=False)
    return response