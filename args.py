from getopt import getopt, GetoptError
import sys

def treat_args(argv):

    
    help_string = '-c <diretorioDadosClientes> -t <diretorioDadosTaxas>'
    arquivo_clientes = ''
    arquivo_taxas = ''

    try:
        opts, args = getopt(argv,'h:c:t:',['help','arquivo_clientes=','arquivo_taxas='])
    except Exception:
        print(help_string)
        exit()

    if len(args) != 0 or (len(opts) == 0 and len(args) == 0):
        print(help_string)
        exit()
    
    for opt, arg in opts:

        if opt in ['-c', '--arquivo_clientes']:
            arquivo_clientes = arg
        elif opt in ['-t', '--arquivo_taxas']:
            arquivo_taxas = arg
        else:
            print(help_string)
            exit()

    return arquivo_clientes, arquivo_taxas