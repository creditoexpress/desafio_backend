FROM mongo:4.0.8


ADD ./repository/ /data/repository/
ADD ./scripts/ /bin/

# COPY ./scripts/ /docker-entrypoint-initdb.d/


RUN chmod +x /bin/mongo-exec.sh

# RUN sh /bin/mongo-exec.sh
CMD ["./bin/mongo-exec.sh"]


#db.createUser({ user: "credexpf", pwd: "111222", roles: [ { role: "readWrite", db: "desafio" } ]})