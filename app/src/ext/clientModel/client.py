from flask import session
from src.ext.parameters import param_ext as pp


def getClient(objClient,db):   
    cliente = db.clientes.find_one(objClient)

    if cliente is None:
            session['cpf'] = False
            session['cel'] = False        
            return {}
            

    session['cpf'] = cliente['cpf']
    session['cel'] = cliente['celular']            

    return {
        'nome': cliente['nome'],
        'score' : cliente['score'],
        'negativado' : cliente['negativado']        
    }


def simulate(value,plots,db):

    categoriesClient = ['NEGATIVADO', 'SCORE_BAIXO', 'SCORE_ALTO']    
    # return {
    #     "a" : session['cpf'], "b": session['cel']
    # }
    client = {"nome": "N/A", "score":0, "negativado": False, 'categoria' :categoriesClient[1]}

    clientJson = False
    
    if session:
        clientJson = pp.parse_param_to_json(['cpf','celular'],session['cpf'],session['cel'])    

    if(clientJson):
        client = db.clientes.find_one(clientJson)            

        if not (client is  None):
            client['categoria'] = categoriesClient[1]        
            
            if client['negativado']:
                client['categoria'] = categoriesClient[0]
            elif client['score'] > 500:
                client['categoria'] = categoriesClient[2]
    
    taxaObj = db.taxas.find_one({"tipo" : client['categoria']})
    # return {"taxa" : taxaObj['taxas'], "plots": plots, "pl" : taxaObj['taxas'][str(plots)]}

    tax = taxaObj['taxas'][str(plots)]
    acctax = float(tax)+1
    
    value = float(value)
    vf = value*acctax
    
    parcela = round((vf/float(plots)),2)
# {"numeroParcelas":12,"outrasTaxas":85,"total":10485.0,"valorJuros":400.0,"valorParcela":873.75,"valorSolicitado":10000}

    return {        
            "valorSolicitado" : value,
            "numeroParcelas" : plots,        
            "taxa" : tax,
            "total" : vf,
            "valorJuros" : (vf- value),
            "valorParcela" : parcela,
            "client":{
                'nome': client['nome'],
                'score' : client['score'],
                'negativado' : client['negativado']      
            }         
        }