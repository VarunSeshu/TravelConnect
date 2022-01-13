from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String
from sqlalchemy.sql.expression import func
from .stores import Stores

from . import Base


class Owners(Base):

    __tablename__ = "owners"

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255))
    home_address = Column(String(500))
    store_id = Column(BigInteger, ForeignKey(Stores.id), nullable=False)
    contact_no = Column(String(15))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
