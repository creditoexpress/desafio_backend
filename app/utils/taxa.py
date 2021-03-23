from models import Taxa

def return_taxa_json( func ):
    def a( *args, **kwargs ):
        return Taxa.to_json( func( *args, **kwargs ) )
    return a