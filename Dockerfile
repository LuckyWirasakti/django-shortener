FROM python:3.8.7
LABEL maintainer="lucky.wirasakti@icloud.com"

# env var
ENV PYTHONUNBUFFERED=1

# copy host to container
COPY . /code/

# working direcory
WORKDIR /code/

# install module third party
RUN pip install -r requirements.txt

# expose port
EXPOSE 8000

# start bash command
ENTRYPOINT ["sh","start.sh"]