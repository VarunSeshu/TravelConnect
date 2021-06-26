# Backend Template
Template build on top of fastapi , dynamodb.
```
This includes logging and sentry setup also.

local Dynamodb  is used for devlopment.
```
# Running on Docker

```
docker-compose up
command to go inside backend container: 
docker exec -it backend-template_backend_service_1 bash
```

# Additional info :
```
dynamodb runs on port 8000
Fastapi runs on port 5000
```
# Dynamodb usage example using awscli:
```
aws dynamodb list-tables  --endpoint-url http://dynamodb-local:8000 --region us-west-2
```