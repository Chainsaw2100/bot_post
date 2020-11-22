FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y software-properties-common
RUN apt-add-repository -y universe
RUN apt-get install -y python3-pip python-dev build-essential
COPY . /app
WORKDIR /app 
RUN pip3 install -r requirements.txt
ENTRYPOINT ['python']
CMD ['app.py']
EXPOSE 5000
EXPOSE 2376