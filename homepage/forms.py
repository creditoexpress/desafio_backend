from django import forms


class ValidarClienteForm(forms.Form):
    cpf = forms.IntegerField(required=True, label='',
                             help_text="CPF - Apenas números."
                             )

    celular = forms.IntegerField(
        label='', required=True, help_text='Celular - Apenas números.')


PARCELAS = (
    ("6", "6"),
    ("12", "12"),
    ("18", "18"),
    ("24", "24"),
    ("36", "36"),
)


class simularTaxaForm(forms.Form):
    valor = forms.DecimalField(
        label='', required=True, help_text='Valor do empréstimo.')
    parcelas = forms.MultipleChoiceField(
        label='', required=True, choices=PARCELAS, help_text='Número de parcelas.',
    )
