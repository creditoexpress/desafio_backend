from repository import taxa as taxa_repository

from service import tipo_taxa as tipo_taxa_service
from models.taxa import ID_TIPO_TAXA, JUROS, NUM_PARCELAS

def insert_taxa( taxa ):
    return taxa_repository.insert_taxa( taxa )

def build_taxas_list( taxas: dict, id_tipo_taxa ):
    taxas_list = list()
    for num_parcelas, juros in zip( taxas.keys(), taxas.values() ):
        taxa = build_taxa_dict( num_parcelas, juros, id_tipo_taxa )
        taxas_list.append( taxa )
    
    return taxas_list

def build_taxa_dict( num_parcelas, juros, id_tipo_taxa ):
    taxa = dict()
    taxa[ NUM_PARCELAS ] = int( num_parcelas )
    taxa[ JUROS ] = float( juros )
    taxa[ ID_TIPO_TAXA ] = id_tipo_taxa
    
    return taxa

def get_val_juros_by_tipo_taxa_and_parcelas( tipo_taxa, num_parcelas ):
    id_tipo_taxa = tipo_taxa_service.get_id_tipo_taxa( tipo_taxa )
    taxa = taxa_repository.find_taxa_by_num_parcelas_and_id_tipo_taxa( id_tipo_taxa, num_parcelas )
    
    return taxa.juros

