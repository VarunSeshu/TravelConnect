from black import re
from pytest_mock import session_mocker
from src.models import owners
from src.models.users import Users
from src.models.customers import Customers
from src.models.owners import Owners
from src.models.stores import Stores
from src.models.business_categories import BusinessCategories
import logging
from src.database.db import db_session

db_session = db_session()
logger = logging.getLogger("backend")


class DbRepositories:
    def __init__(self, user_id):
        self.user_id = user_id

    def get_main_user(self):
        return Users.get({"id": self.user_id}).first()

    def update_main_user_details(self, request):
        Users.update(
            {"id": self.user_id}, name=request.name, home_address=request.home_address
        )
        logger.info("Updated main user's details")

    def create_new_customer(self, request):
        customer = Customers.get({"user_id": self.user_id}).first()
        if not customer:
            customer = Customers.create(
                user_id=self.user_id, home_address=request.home_address
            )
            logger.info(f"Created new customer {customer}")
        return customer

    def create_new_store(self, request):
        store = Stores.get({"name": request.store_name}).first()
        if not store:
            business_cat_id = self.get_business_category(request.store_category_name)
            store = Stores(
                name=request.store_name,
                business_category_id=business_cat_id,
                address=request.store_address,
                description=request.store_description,
            )
            db_session.add(store)
            db_session.flush()
            logger.info(f"Created new customer {store}")
        return store

    def get_business_category(self, category_name):
        item = BusinessCategories.get({"name": category_name}).first()
        if not item:
            raise Exception("Item with category name not found")
        return item.id

    def create_new_owner(self, store_id):
        owner = Owners.get({"user_id": self.user_id}).first()
        if not owner:
            owner = Owners.create(user_id=self.user_id, store_id=store_id)
            logger.info(f"Created new customer {owner}")
        return owner
