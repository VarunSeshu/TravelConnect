from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String
from sqlalchemy.sql.expression import func
from .users import Users
from . import Base


class Customers(Base):

    __tablename__ = "customers"

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey(Users.id), nullable=False)
    home_address = Column(String(500))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
