from rest_framework import serializers
from clientes.models import Clientes


class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = ('id', 'nome', 'cpf', 'celular', 'score', 'negativado')
        extra_kwargs = {

            'cpf': {'write_only': True, 'required': True, },
            # 'score': {'write_only': True, 'required': True, }, #TODO REMOVE COMMENTS
            # 'negativado': {'write_only': True, 'required': True, },
            'celular': {'write_only': True, 'required': True}
        }
