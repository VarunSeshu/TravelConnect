import logging
import os

from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder

from src.api.schema.request import RequestModel
from src.api.schema.response import ResponseModel
from src.lib.logging.logger import add_param

os.path.join(os.getcwd(), "src")

router = APIRouter()


#######################################
#       Backend APIS              #
#######################################
log = logging.getLogger("backend")


@router.post("/test", response_model=ResponseModel)
async def test(request: RequestModel, auth_request: Request):
    log.debug(f"Backend Test API : {jsonable_encoder(request)}")
    message = f"Test API hit by {request.name}  with message {request.message}"
    add_param("user_name", request.name)
    log.info(message)
    return ResponseModel(return_message=message)
