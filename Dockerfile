FROM python:3.12.0

COPY Pipfile Pipfile.lock settings.yaml ./

RUN pip install pipenv && pipenv install --deploy

COPY app ./app
COPY domain ./domain
