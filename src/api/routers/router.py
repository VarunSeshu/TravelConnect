import logging
import os

from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder

from src.api.schema.response import LoginResponse
from src.modules.login import Login

os.path.join(os.getcwd(), "src")

router = APIRouter()


#######################################
#       Backend APIS              #
#######################################
log = logging.getLogger("backend")


@router.post("/login/{user_id}", response_model=LoginResponse)
def login(user_id: int):
    log.info(f"Login API request : {jsonable_encoder(user_id)}")
    access_token = Login(user_id).get_access_token()
    if access_token:
        return LoginResponse(success=True, access_token=access_token)
    return LoginResponse(success=False)


@router.get("/user")
def user(auth_request: Request):
    return {"user": auth_request.state.user_id}
