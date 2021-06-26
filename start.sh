#!/bin/bash
# sed -i -e "s/APP_ENV/${APP_ENV}/g" /etc/filebeat/filebeat.yml
# sed -i -e "s|ES_HOST_URL|${ES_HOST_URL}|g" /etc/filebeat/filebeat.yml
# sed -i -e "s/ES_USERNAME/${ES_USERNAME}/g" /etc/filebeat/filebeat.yml
# sed -i -e "s/ES_PASSWORD/${ES_PASSWORD}/g" /etc/filebeat/filebeat.yml
# service filebeat start
# Running migrations
if [ $? -ne 0 ]; then
    echo 'Error in running database migrations'> server_uvicorn.log
    exit 1
fi
/usr/local/bin/uvicorn src:app --host 0.0.0.0 --port 5000 --reload --log-level info > server_uvicorn.log
