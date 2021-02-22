FROM ruby:2.6-buster

RUN apt-get update -qq

ARG BUILD_RAILS_ENV
# Prepara aplicacão
###################################
RUN mkdir /credito_express
WORKDIR /credito_express

# instala bundler e configura bundler para produção
RUN gem install bundler -v 2.2.8 && if [ "$BUILD_RAILS_ENV" = "production" ]; \
then \
	bundle config frozen true \
	&& bundle config --local without development:test; \
fi

# copia gemfile e lock para sabermos quais gems instalar
COPY Gemfile Gemfile.lock ./

# install gems
RUN bundle install --jobs 20 --retry 5 \
	&& rm -rf /usr/local/bundle/cache/*.gem \
	&& find /usr/local/bundle/gems/ -name "*.c" -delete \
	&& find /usr/local/bundle/gems/ -name "*.o" -delete

# copy app
COPY . ./

# adiciona a pasta bin ao path (para poder rodar respec, por exemplo)
ENV PATH="/credito_express/bin:${PATH}"

# Add a script to be executed every time the container starts.
COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]

# Roda aplicacão
###################################
CMD bundle exec rails s -p $PORT -b '0.0.0.0'
