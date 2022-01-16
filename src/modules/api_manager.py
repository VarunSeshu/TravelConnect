from src.api.schema.response import LoginResponse, APIStatusResponse
from src.api.schema.request import SendOTPRequest
from src.modules.authentication import Login, OtpController
from src.database.db import db_session
from src.models.users import Users
import logging

logger = logging.getLogger("backend")
db_session = db_session()


def login_user(user_id):
    access_token = Login(user_id).get_access_token()
    if access_token:
        return LoginResponse(success=True, access_token=access_token)
    return LoginResponse(success=False)


def send_otp_to_user(request):
    is_sent = OtpController(request.phone_no).send_otp()
    return APIStatusResponse(success=is_sent)


def verify_otp_and_return_user_and_token(request):
    is_valid = OtpController(request.phone_no).verify_otp(request.otp)
    if not is_valid:
        return APIStatusResponse(success=False)
    response = {}
    response["user"] = fetch_or_create_user(request.phone_no)
    response["token"] = login_user(response["user"].id)
    return response


def fetch_or_create_user(phone_no):
    user = db_session.query(Users).filter(Users.contact_no == phone_no).first()
    if not user:
        logger.info(
            f"No existing user found. Creating new User with phone_no {phone_no}"
        )
        user = Users(contact_no=phone_no)
        db_session.add(user)
        db_session.flush()
    return user
