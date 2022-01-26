from sqlalchemy import BigInteger, Column, DateTime, ForeignKey
from sqlalchemy.sql.expression import func
from .product_categories import ProductCategories
from .business_categories import BusinessCategories
from .parent_model import ParentModel

from . import Base


class ProductBusinessMap(Base, ParentModel):

    __tablename__ = "product_business_map"

    id = Column(BigInteger, primary_key=True)
    product_category_id = Column(
        BigInteger, ForeignKey(ProductCategories.id), nullable=False
    )
    business_category_id = Column(
        BigInteger, ForeignKey(BusinessCategories.id), nullable=False
    )
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
