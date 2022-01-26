from sqlalchemy import BigInteger, Column, DateTime, String
from sqlalchemy.sql.expression import func
from .parent_model import ParentModel

from . import Base


class BusinessCategories(Base, ParentModel):

    __tablename__ = "business_categories"

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
