from flask import jsonify,request, session
from src.ext.parameters import param_ext as pp
from src.ext.clientModel import client as cl


def init_app(app,db):

    @app.route('/')
    def index():        
        return jsonify(
            status=True,
            cpf = session['cpf'],
            celular = session['cel'],
        )

    @app.route('/findClient')
    def findClient():
        
        cpf = request.args.get('cpf') 
        cel = request.args.get('celular') 

        objFind = pp.parse_param_to_json(['cpf','cel'],cpf,cel)
        
        if not objFind:
            return jsonify(
                status=True,
                message= "cpf or celular is required")
        

        return jsonify(
            status=True,
            data=cl.getClient(objFind,db)
        )

       
    @app.route('/simular',methods=['post'])
    def simular():
        content = request.json
        if not content:
            return jsonify(
                status = False,
                data = "Parametros invalidos"
            )
            
        value = content['valor']
        plots = content['numeroParcelas']        
        
        params = pp.verify_params_simulacao(value,plots)
        erro = params['erro']
        
        if erro:
            return jsonify(
                status = False,
                data = params['msg']
            )
        
        data = cl.simulate(value,plots,db)

        return jsonify(
            status=True,
            data=data
        )
