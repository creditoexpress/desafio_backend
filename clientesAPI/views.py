from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from clientes.models import Clientes
from .serializer import ClientesSerializer
from rest_framework import viewsets


class ClientesViewSet(viewsets.ModelViewSet):
    """
    Express Client API
    """
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

    def retrieve(self, request, *args, **kwargs):
        params = kwargs

        params_list = params['pk'].split('-')
        cpf = params_list[0]
        celular = params_list[1]

        cliente = Clientes.objects.filter(cpf=cpf, celular=celular)
        serializer = ClientesSerializer(cliente, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # Desabilita CREATE/POST methods
    def create(self, request, *args, **kwargs):
        response = {"message": "Método POST não autoriazado."}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # Desabilita UPDATE/PUT methods
    def update(self, request, *args, **kwargs):
        response = {"message": "Método PUT não autoriazado."}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
