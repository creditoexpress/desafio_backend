# Create env files helper function
create_env_file () {
    [ ! -f ./$1 ] \
    && cp $1.example $1 && echo "File [ $1 ] successfully created!"  \
    || echo "File [ $1 ] already exists."
}

# Creates dotenv file
ENV_FILE=.env
create_env_file $ENV_FILE

# Creates dotenv file for database
DB_ENV_FILE=.env.database
create_env_file $DB_ENV_FILE
