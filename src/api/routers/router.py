import logging
import os

from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder

from src.api.schema.response import LoginResponse, APIStatusResponse
from src.api.schema.request import SendOTPRequest, VerifyOTPRequest
from src.modules.api_manager import (
    login_user,
    send_otp_to_user,
    verify_otp_and_return_user_and_token,
)

os.path.join(os.getcwd(), "src")

router = APIRouter()


#######################################
#       Backend APIS              #
#######################################
log = logging.getLogger("backend")


@router.post("/login/{user_id}", response_model=LoginResponse)
def login(user_id: int):
    log.info(f"Login API request : {jsonable_encoder(user_id)}")
    return login_user(user_id)


@router.get("/user")
def user(auth_request: Request):
    return {"user": auth_request.state.user_id}


@router.post("/send_otp", response_model=APIStatusResponse)
def send_otp(request: SendOTPRequest):
    log.info(f"Send_otp API request : {jsonable_encoder(request)}")
    return send_otp_to_user(request)


@router.post("/verify_otp")
def verify_otp(request: VerifyOTPRequest):
    log.info(f"verify_otp API request : {jsonable_encoder(request)}")
    return verify_otp_and_return_user_and_token(request)
