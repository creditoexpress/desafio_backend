from rest_framework import views, status
from rest_framework.response import Response
from utils.getTaxa import getTaxa
from utils.getTipo import getTipo
from clientes.models import Clientes


class TaxaCalc(views.APIView):

    def get(self, request, pk, str):
        params = str
        params_list = params.split('-')
        numeroParcelas = int(params_list[0])
        meses = params_list[0]
        valor = int(params_list[1])
        taxa = 0

        if pk == 0:
            pk = 'anonimo'
            cliente = ''
            tipo = getTipo(cliente)
            taxa = getTaxa(tipo)
        else:
            cliente = Clientes.objects.get(id=pk)
            tipo = getTipo(cliente)
            taxa = getTaxa(tipo, meses)

        dados = [{
            'numeroParcelas': numeroParcelas,
            'valor': valor,
            'taxaJuros': taxa,
            'jurosMensal': taxa * valor,
            'jurosTotal': taxa * valor * 12,
            'custoFinal': (valor * taxa)*12 + valor
        }]

        return Response(dados, status=status.HTTP_200_OK)
