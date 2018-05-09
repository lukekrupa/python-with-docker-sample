FROM python:3.6.5-alpine

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Bundle app source
COPY . /usr/src/app

ENTRYPOINT [ "python", "source" ]