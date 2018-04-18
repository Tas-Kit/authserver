 FROM python:2
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /authserver
 WORKDIR /authserver
 ADD requirements.txt /authserver/
 RUN pip install --upgrade pip
 RUN pip install -r requirements.txt
 RUN apt-get update
 RUN apt-get install -y gettext
 ADD . /authserver/