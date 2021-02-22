from rest_framework import serializers


class TaxasSerializers(serializers.Serializer):
    numeroParcelas = serializers.IntegerField()
    valor = serializers.IntegerField()
    taxaJuros = serializers.FloatField()
    jurosMensal = serializers.FloatField()
    jurosTotal = serializers.FloatField()
    custoFinal = serializers.FloatField()
