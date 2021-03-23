from mongoengine import connect

def init_db():
    connect( host = 'mongodb://mymongo:27017/credito_express' )
    