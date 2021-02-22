from clientes.models import Clientes
from django.shortcuts import redirect, render
from .forms import ValidarClienteForm, simularTaxaForm
import requests
import json



def homepage(request):

    form = ValidarClienteForm()
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = ValidarClienteForm(request.POST or None)
        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            celular = form.cleaned_data['celular']
            dados = str(cpf) + '-' + str(celular)
            r = requests.get('http://127.0.0.1:8000/clientes/api/v1/' + dados)
            cliente = r.json()
            context['cliente'] = cliente

    return render(request, 'index.html', context)


def simularFinanciamento(request, pk):
    cliente = Clientes.objects.get(id=pk)
    form = simularTaxaForm()
    id = str(cliente.id)
    context = {
        'form': form,
        'cliente': cliente
    }

    if request.method == 'POST':
        form = simularTaxaForm(request.POST or None)
        if form.is_valid():
            valor = str(form.cleaned_data['valor'])
            parcelas = str(form.cleaned_data['parcelas'][0])
            r = requests.get('http://127.0.0.1:8000/taxas/api/v1/' +
                             id + '/' + parcelas + '-' + valor)
            resultado = r.json()
            context['resultado'] = resultado

    return render(request, 'simular.html', context)


def importar(request):
    queryset = Clientes.objects.all()
    with open('clientes.json') as json_file:
        data = json.loads(json_file.read())
        for cliente in data:
            if not cliente['cpf'] in queryset:
                Clientes.objects.create(
                    nome=cliente['nome'],
                    cpf=cliente['cpf'],
                    celular=cliente['celular'],
                    score=cliente['score'],
                    negativado=cliente['negativado']
                )
    return redirect('homepage')