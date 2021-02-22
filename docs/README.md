# Simulations API

This is an API that simulates loans for interested people over the best taxes in the market.

## Prerequisites

- Docker
- Docker-compose

**Optional**

- Bash / Shell terminal

## Setup

If you are using a shell script terminal, just run the command below to bootstrap the setup files

```bash
$ make setup-linux
```

That will :

1. create the files `.env` and `.env.database` as in the example files
   > Case you want to create them yourself, just replicate the content of the files to new files with the names mentioned above.
2. Create the `.venv` folder for your virtual environment
3. Activate it
4. Download poetry package manager
5. Add it to your cli

After that, to install the dependencies you must execute the command below

```bash
$ poetry install
```

## Seeders

To run the seeders run the command
```bash
$ make seeds
```


## Run

To run the project just execute de command below or an equivalent to execute the `docker-compose` file

```bash
$ docker-compose up -d
```

That will initiate the services database and apis.