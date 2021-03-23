import traceback, logging

from service import taxa as taxa_service, tipo_taxa as tipo_taxa_service

from models.tipo_taxa import JSON_TIPO, JSON_TAXAS
from models.taxa import ID_TIPO_TAXA

def insert_taxas( taxas ):
    try:
        for taxa in taxas:
            tipo_taxa = taxa[ JSON_TIPO ]
    
            id_tipo_taxa = tipo_taxa_service.find_tipo_taxa( tipo_taxa )
            if id_tipo_taxa is None:
                id_tipo_taxa = tipo_taxa_service.insert_tipo_taxa( tipo_taxa ).id
            else:
                id_tipo_taxa = id_tipo_taxa.id

            taxas_list = taxa_service.build_taxas_list( taxa[ JSON_TAXAS ], id_tipo_taxa )

            for taxa in taxas_list:
                taxa_service.insert_taxa( taxa )

    except Exception as e:
        logging.error( traceback.format_exc() )
        return "Falha ao inserir taxas", 500

    else:
        return "Inserção de taxas efetuada com sucesso", 200
