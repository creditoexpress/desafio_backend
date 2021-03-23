class Emprestimo():
    id_usuario = int()
    val_emprestimo = float()
    numParcelas = int()

    def __init__( self, id_usuario, val_emprestimo, num_parcelas ):
        self.id_usuario = id_usuario
        self.val_emprestimo = val_emprestimo
        self.num_parcelas = num_parcelas

#ATRIBUTOS JSON
NUM_PARCELAS = 'numeroParcelas'
VAL_EMPRESTIMO = 'valor'