from djongo import models


class Clientes(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    celular = models.CharField(max_length=11)
    score = models.CharField(max_length=3)
    negativado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f'{self.nome}'
