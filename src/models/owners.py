from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String
from sqlalchemy.sql.expression import func
from .stores import Stores
from .users import Users
from . import Base


class Owners(Base):

    __tablename__ = "owners"

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey(Users.id), nullable=False)
    store_id = Column(BigInteger, ForeignKey(Stores.id), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
