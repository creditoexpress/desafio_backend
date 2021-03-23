import traceback

from models.emprestimo import Emprestimo, NUM_PARCELAS, VAL_EMPRESTIMO
from service import user as user_service, tipo_taxa as tipo_taxa_service, taxa as taxa_service, emprestimo as emprestimo_service

def simular_emprestimo( user_id, emprestimo ):
    try:
        emprestimo = Emprestimo( user_id, emprestimo[ VAL_EMPRESTIMO ], emprestimo[ NUM_PARCELAS ] )

        user_tipo_taxa = user_service.get_tipo_taxa_user_by_user_id( user_id )
        taxa_juros = taxa_service.get_val_juros_by_tipo_taxa_and_parcelas( user_tipo_taxa, emprestimo.num_parcelas )

        response = emprestimo_service.calular_emprestimo_request( emprestimo, taxa_juros )

        return response
    except Exception as e:
        traceback.print_exc()

        return "Error ao simular emprestimo", 505
