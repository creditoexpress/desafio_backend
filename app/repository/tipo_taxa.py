from models import Tipo_taxa

def insert_tipo_taxa( descr_taxa ):
    tipo_taxa = Tipo_taxa( descr = descr_taxa )
    tipo_taxa.save()
    return tipo_taxa

def find_tipo_taxa( descr_taxa ):
    return Tipo_taxa.objects( descr = descr_taxa ).first()