from sqlalchemy import BigInteger, Column, DateTime, String
from sqlalchemy.sql.expression import func


from . import Base


class ProductCategories(Base):

    __tablename__ = "product_categories"

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
