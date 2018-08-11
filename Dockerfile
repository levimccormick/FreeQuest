FROM python:3.7-alpine

RUN adduser -D freequest
WORKDIR /home/freequest

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

COPY . .

RUN pip install pipenv
RUN pipenv install --deploy --system

RUN chown -R freequest:freequest ./
USER freequest

ENTRYPOINT [ "freequest" ]