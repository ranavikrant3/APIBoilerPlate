FROM python:3.7.4-slim-buster

# Set the global packages for the app server
RUN apt-get update
RUN apt-get install -y --no-install-recommends  build-essential gcc supervisor net-tools curl gnupg nginx

# Microsoft SQL Server Prerequisites
ENV ACCEPT_EULA=Y
RUN apt-get update \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/9/prod.list \
        > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get install -y --no-install-recommends \
        locales \
        apt-transport-https \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen \
    && apt-get update \
    && apt-get -y --no-install-recommends install \
        unixodbc-dev \
        msodbcsql17

# Copy the Supervisor global configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# App Server environment setting
ENV HOME=/app
RUN mkdir ${HOME}/
WORKDIR ${HOME}/

# install dependencies
COPY requirements.txt ${HOME}/
RUN pip install --upgrade pip -r requirements.txt

COPY . /app

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]