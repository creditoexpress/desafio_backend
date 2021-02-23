# Simulations API

This is an API that simulates loans for interested people over the best taxes in the market.

## Prerequisites

- Docker
- Docker-compose

**Optional**

- Makefile
- Bash / Shell terminal

## Setup

If you are using a shell script terminal, just run the command below to bootstrap the setup files.

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

This setup was done in a linux OS, so in windows or MAC it might differ, however, in case you are interested in reproducing those steps by hand, you can do so by:

1. Executing the `.env` file instructions right above
2. Installing and activating poetry in your shell terminal (not necessary if you'll not use the seeders)

After that, to install the dependencies you must execute the command below

```bash
$ poetry install
```

## Seeders

To run the seeders run the command

```bash
$ make seeds
```

The seeders require certain dependencies to be installed, that's why the setup script create a `virtualenv` and install the dependencies on it.

## Run

To run the project just execute de command below or an equivalent to execute the `docker-compose` file

```bash
$ docker-compose up -d
```

That will initiate the services database and apis.

## Docs

The API docs are in the addresses `http://localhost:5000/redoc` or `http://localhost:5000/docs` after the container is running.

PS: For some reason, the docs of the simulate API are not showing, so, you can use insomnia to execute the requests, or, hit the url `http://localhost:5000/simulate` with a payload such as:

```json
{
   "portions": 12,
   "value": 10000.0
}
```

## Run tests using insomnia

The scenarios of test are all covered, but so far I have not made integration nor unitary tests.
To at least help with that, there is a file called `Insomnia_2021_02_22` in the root of the project,
which can be imported and execute the requests.

## Built with

- [FastAPI](https://fastapi.tiangolo.com/) - Web Framework
- [Motor](https://motor.readthedocs.io/en/stable/) - Async MongoDB Client
- [Dotenv](https://pypi.org/project/python-dotenv/) - Env files loader
- [Docker](https://www.docker.com/) - Virtualizer of containers
- [Docker-Compose](https://docs.docker.com/compose/) - Containers manager
- [Shell Script](https://www.shellscript.sh/) - To create scripts for tasks automation
- [Makefile](https://opensource.com/article/18/8/what-how-makefile) - To help with tasks execution like seeding the database or bootstraping the dev environment
- [Poetry](https://python-poetry.org/) - Dependency manager and scripts helper somewhat cli alike
- [http3](https://pypi.org/project/http3/) - For async requests since Fastapi uses an event loop model with uvicorn implemented over uvloop
