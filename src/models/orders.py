from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String, Enum
from sqlalchemy.sql.expression import func
from sqlalchemy.dialects.mysql import INTEGER
from .customers import Customers
from .stores import Stores
from src.config.enums import OrderStatus
from . import Base


class Orders(Base):

    __tablename__ = "orders"

    id = Column(BigInteger, primary_key=True)
    customer_id = Column(BigInteger, ForeignKey(Customers.id), nullable=False)
    store_id = Column(BigInteger, ForeignKey(Stores.id), nullable=False)
    total_amount = Column(INTEGER)
    status = Column(Enum(OrderStatus))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
