from ast import Store
from black import re
from pytest_mock import session_mocker
from src.models.users import Users
from src.models.customers import Customers
from src.models.owners import Owners
from src.models.stores import Stores
from src.models.products import Products
from src.models.product_details import ProductDetails
from src.models.business_categories import BusinessCategories
import logging
from sqlalchemy import func
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
            logger.info(f"Created new Store {store}")
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

    def create_new_product(self, request):
        product = (
            db_session.query(Products)
            .filter(
                func.lower(Products.name) == func.lower(request.product_name),
                Products.store_id == request.store_id,
            )
            .first()
        )
        if product:
            logger.info(f"The product already exists with name {request.product_name}")
            raise Exception("Product already exists")
        product = Products(
            name=request.product_name,
            brand=request.product_brand,
            description=request.product_description,
            store_id=request.store_id,
        )
        db_session.add(product)
        db_session.flush()
        return product

    def add_product_details(self, request, product_id):
        for details in request.product_details:
            product_details = ProductDetails(
                product_id=product_id,
                unit=details.unit,
                actual_price=details.mrp_price,
                discounted_price=details.discounted_price,
                quantity=details.quantity,
            )
            db_session.add(product_details)
            db_session.flush()
        return True

    def delete_customer(self):
        Customers.delete({"user_id": self.user_id})

    def delete_store(self):
        owner = Owners.get({"user_id": self.user_id}).first()
        if owner:
            Stores.delete({"id": owner.store_id})

    def delete_owner(self):
        Owners.delete({"user_id": self.user_id})

    def delete_user(self):
        Users.delete({"id": self.user_id})
