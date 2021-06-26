FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
RUN apt-get update
# Install base python dependencies
# RUN apt-get install build-essential libssl-dev libffi-dev -y
RUN python -m pip install --upgrade pip==20.2.4\
    && pip install awscli
RUN echo "export PS1='\[\e[38;5;202m\]\[\e[38;5;245m\]\u\[\e[00m\]@\[\e[38;5;172m\]backend[C]\[\e[00m\]:\[\e[38;5;5m\]\W\[\e[00m\]\\$ '" >> ~/.bashrc
RUN apt-get install vim curl -y
RUN curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-6.8.12-amd64.deb && dpkg -i ./filebeat-6.8.12-amd64.deb
COPY ./docker/filebeat.yml /etc/filebeat/filebeat.yml
RUN chmod go-w /etc/filebeat/filebeat.yml
# Copy python dependencies file
ADD requirements.txt ./
# Install python packages
#RUN pipenv install --deploy --ignore-pipfile --dev --system
# Copy source code
RUN pip install -r requirements.txt
COPY ./ /usr/src/backend
WORKDIR /usr/src/backend
EXPOSE 5000
CMD [ "sh", "/usr/src/backend/start.sh" ]
