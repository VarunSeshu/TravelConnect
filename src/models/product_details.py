from ast import In
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String, Enum
from sqlalchemy.sql.expression import func
from sqlalchemy.dialects.mysql import INTEGER
from .products import Products
from .orders import Orders
from src.config.enums import Units
from . import Base
from .parent_model import ParentModel


class ProductDetails(Base, ParentModel):

    __tablename__ = "product_details"

    id = Column(BigInteger, primary_key=True)
    product_id = Column(BigInteger, ForeignKey(Products.id), nullable=False)
    unit = Column(Enum(Units))
    actual_price = Column(INTEGER)
    discounted_price = Column(INTEGER)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
