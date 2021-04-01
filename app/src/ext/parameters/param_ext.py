def parse_param_to_json(keys,value1,value2):

    objFind = {}
    
    if not value1 and not value2:
        return False 
    
    if value1:
        objFind[keys[0]] = value1

    if value2:
        objFind[keys[1]] = value2
    
    return objFind




def verify_params_simulacao(value,plots):
    possiblePlots = [6,12,18,24,36]    

    if( not value or not plots):       
        return {
            'erro':True,
            'msg':"value and plots is required"
        }
    
    value = float(value)
    plots = int(plots)

    if value < 0 or plots not in possiblePlots:
        return {
            'erro':True,
            'msg':"value must to be more than 0, and plots 6,12,18,24 or 36 "
        }
    
    return {
        'erro': False, 
        'param' : {
            'value' : value,
            'plots' : plots
            }
        }