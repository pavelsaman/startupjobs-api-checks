FROM python:3.9-slim-buster

LABEL author="Pavel Saman"
LABEL maintainer="samanpavel@gmail.com"
LABEL description="Docker pytest"
LABEL version="1.0"

# install necessary packages
RUN apt-get update \
    && apt-get -y install \
    && apt-get install -y unixodbc-dev g++ curl gnupg

WORKDIR /tests

# install requirements for the tests
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# create a folder for test results, copy tests
RUN mkdir Results
COPY . .

# create a non-privileged user
RUN groupadd -r pytest \
    && useradd --no-log-init -r -g pytest pytest \
    && chown -R pytest:pytest /tests
USER pytest:pytest

# run tests with pytest
CMD ["pytest"]
