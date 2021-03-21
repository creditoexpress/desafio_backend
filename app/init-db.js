db = db.getSiblingDB("desafio");
db.users.drop();

db.users.insertMany([
  {
    "nome": "Lucca Porto", 
    "cpf": "27031984696", 
    "celular": "81974162642", 
    "score": 770, 
    "negativado": true
  },
  {
    "nome": "Bernardo Martins", 
    "cpf": "23401976516", 
    "celular": "81977468400", 
    "score": 879, 
    "negativado": true
  },
  {
    "nome": "Arthur Caldeira", 
    "cpf": "14329750805", 
    "celular": "31934706786", 
    "score": 358, 
    "negativado": false
  }
]);