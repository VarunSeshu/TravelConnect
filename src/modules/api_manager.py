from src.api.schema.response import LoginResponse, APIStatusResponse
from src.api.schema.request import SendOTPRequest
from src.modules.authentication import Login, OtpController
from src.database.db import db_session
from src.models.users import Users
import logging
from src.database.db_repository import DbRepositories

logger = logging.getLogger("backend")
db_session = db_session()


def login_user(user_id):
    access_token = Login(user_id).get_access_token()
    if access_token:
        return LoginResponse(success=True, access_token=access_token)
    return LoginResponse(success=False)


def send_otp_to_user(request):
    # is_sent = OtpController(request.phone_no).send_otp()
    is_sent = True
    return APIStatusResponse(success=is_sent)


def verify_otp_and_return_user_and_token(request):
    # is_valid = OtpController(request.phone_no).verify_otp(request.otp)
    # if not is_valid:
    #     return APIStatusResponse(success=False)
    response = {}
    response["user"] = fetch_or_create_user(request.phone_no)
    response["token"] = login_user(response["user"].id)
    return response


def fetch_or_create_user(phone_no):
    user = Users.get({"contact_no": phone_no}).first()
    if not user:
        logger.info(
            f"No existing user found. Creating new User with phone_no {phone_no}"
        )
        user = Users(contact_no=phone_no)
        db_session.add(user)
        db_session.flush()
    return user


def update_user_details(request, user_id):
    user = Users.get({"id": user_id}).first()
    if not user:
        logger.info(f"No existing user found. Creating new User with user_id {user_id}")
        return "User Not found"
    # user = Users.update({"id": user_id}, name = "")
    db_repositories = DbRepositories(user_id)
    db_repositories.update_main_user_details(request)
    customer = db_repositories.create_new_customer(request)
    if request.store_name:
        store = db_repositories.create_new_store(request)
        owner = db_repositories.create_new_owner(store.id)
        logger.info(
            f"updated_user details , Customer: {customer}, store: {store}, owner: {owner}"
        )
    logger.info(f"updated_user details , Customer: {customer}")
    return customer


def add_new_product(request, user_id):
    db_repositories = DbRepositories(user_id)
    product = db_repositories.create_new_product(request)
    db_repositories.add_product_details(request, product.id)


def delete_user_and_properties(user_id):
    db_repositories = DbRepositories(user_id)
    db_repositories.delete_customer()
    db_repositories.delete_store()
    db_repositories.delete_owner()
    db_repositories.delete_user()
    return True
