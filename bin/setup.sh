create_env_file () {
    [ ! -f ./.env.database ] \
    && cp .env.database.example .env.database \
    || echo "$1 already exists."
}

# Creates dotenv file
ENV_FILE=.env
create_env_file $ENV_FILE

# Creates dotenv file for database
DB_ENV_FILE=.env.database
create_env_file $DB_ENV_FILE
