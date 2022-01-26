from ast import In
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String
from sqlalchemy.sql.expression import func
from sqlalchemy.dialects.mysql import INTEGER
from .products import Products
from .orders import Orders
from . import Base
from .parent_model import ParentModel


class OrderDetails(Base, ParentModel):

    __tablename__ = "order_details"

    id = Column(BigInteger, primary_key=True)
    order_id = Column(BigInteger, ForeignKey(Orders.id), nullable=False)
    product_id = Column(BigInteger, ForeignKey(Products.id), nullable=False)
    quantity = Column(INTEGER)
    amount = Column(INTEGER)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
