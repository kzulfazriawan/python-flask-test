# #python-flask-test

This is simple project for flask based on my half-progress [Micro-Framework Metric](https://github.com/metric-python/metric).

## Quickstart
#### Requirements

 - Docker and docker compose
 - NodeJS with NPM
 - Python 3.6 above
 
#### Installation
 - build the Dockerfile `$ docker compose build`
 - run the docker-compose.yaml `$ docker compose run`
 - run the migration `$ docker compose run --rm web alembic upgrade head`
 - start the API by hit CURL *http://localhost:8000*
