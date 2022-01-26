from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String
from sqlalchemy.sql.expression import func
from .business_categories import BusinessCategories
from .parent_model import ParentModel
from . import Base


class Stores(Base, ParentModel):

    __tablename__ = "stores"

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255))
    business_category_id = Column(
        BigInteger, ForeignKey(BusinessCategories.id), nullable=False
    )
    address = Column(String(500))
    description = Column(String(500))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
