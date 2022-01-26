from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String
from sqlalchemy.sql.expression import func
from sqlalchemy.dialects.mysql import TINYINT
from .product_categories import ProductCategories
from .stores import Stores
from .parent_model import ParentModel
from . import Base


class Products(Base, ParentModel):

    __tablename__ = "products"

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255))
    product_category_id = Column(
        BigInteger, ForeignKey(ProductCategories.id), nullable=False
    )
    brand = Column(String(255))
    store_id = Column(BigInteger, ForeignKey(Stores.id), nullable=False)
    image = Column(String(500))
    description = Column(String(500))
    in_stock = Column(TINYINT, nullable=False, default=1)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
