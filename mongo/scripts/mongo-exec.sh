#!/bin/sh
for c in clientes taxas
do  
  mongoimport --db desafio --authenticationDatabase admin  --collection $c --type json --username credexpm  --password 111222 --drop --file /data/repository/$c.json --jsonArray
done

