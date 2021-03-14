# base image from docker hub
FROM python:3.8.7

# meta desc for information 
LABEL maintainer="lucky.wirasakti@icloud.com"

# env var
ENV PYTHONUNBUFFERED=1

# copy host to container
COPY . /code/

# working direcory
WORKDIR /code/

# install module third party
RUN pip install -r requirements.txt

# install os third party
RUN apt-get update && apt-get install -y gettext 

# expose port
EXPOSE 8000

# start entrypoint
ENTRYPOINT ["sh","start.sh"]