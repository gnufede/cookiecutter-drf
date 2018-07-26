FROM python:3.7
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY Pipfile* ./
RUN pip install pipenv
RUN pipenv install --dev --system --deploy --ignore-pipfile

# Adds our application code to the image
COPY . /code/
WORKDIR /code

EXPOSE 8000

# Migrates the database, uploads staticfiles, and runs the production server
CMD ./manage.py migrate && \
    ./manage.py collectstatic --noinput && \
    newrelic-admin run-program gunicorn \
      --bind 0.0.0.0:$PORT \
      --access-logfile \
      - config.wsgi:application
