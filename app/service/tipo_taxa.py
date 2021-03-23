from repository import tipo_taxa as tipo_taxa_repository

def insert_tipo_taxa( tipo_taxa ):
    return tipo_taxa_repository.insert_tipo_taxa( tipo_taxa )

def find_tipo_taxa( tipo_taxa ):
    return tipo_taxa_repository.find_tipo_taxa( tipo_taxa )

def get_id_tipo_taxa( tipo_taxa ):
    tipo_taxa = find_tipo_taxa( tipo_taxa )
    return tipo_taxa.id