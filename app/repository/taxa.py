import json

from models.taxa import Taxa, NUM_PARCELAS, JUROS, ID_TIPO_TAXA
from utils.taxa import return_taxa_json

@return_taxa_json
def insert_taxa( taxa_dict ):
    taxa = Taxa( num_parcelas = taxa_dict[ NUM_PARCELAS ], 
                 juros = taxa_dict[ JUROS ], 
                 id_tipo_taxa = taxa_dict[ ID_TIPO_TAXA ] )
    taxa.save()
    return taxa

def find_taxa_by_num_parcelas_and_id_tipo_taxa( tipo_taxa, parcelas ):
    taxa = Taxa.objects.get( num_parcelas = parcelas, id_tipo_taxa = tipo_taxa )
    return taxa