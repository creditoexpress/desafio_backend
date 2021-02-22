
def getTipo(cliente=''):
    if not cliente:
        return 'SCORE_BAIXO'

    if cliente.negativado == True:
        return 'NEGATIVADO'

    if int(cliente.score) > 500:
        return 'SCORE_ALTO'
    else:
        return 'SCORE_BAIXO'
