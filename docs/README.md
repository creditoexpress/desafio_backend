# Simulations API

This is an API that simulates loans for interested people over the best taxes in the market.

## Prerequisites

- Docker
- Docker-compose

**Optional**

- Bash / Shell terminal

## Setup

If you are using a shell script terminal, just run the command below to bootstrap the setup files

```shell
$ sh bin/setup.sh
```

That will create the files `.env` and `.env.database` as in the example files.

Case you want to create them yourself, just replicate the content of the files to new files with the names mentioned above.

## Run

To run the project just execute de command below or an equivalent to execute the `docker-compose` file

```shell
$ docker-compose up -d
```

That will initiate the services database and api.
