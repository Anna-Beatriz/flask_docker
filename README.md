# flask_docker
Aplicação simples com flask e docker.


# PASSOS:

docker-compose up -d

docker network inspect bridge

docker-compose run web /usr/local/bin/python create_db.py

acessar o programa no navegador e inserir dados

docker ps

docker exec -it <id container do db> /bin/bash

su postgres
  
psql -U dbdocker
  
select * from comentarios;
