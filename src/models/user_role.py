from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String, Enum
from sqlalchemy.sql.expression import func
from .users import Users
from src.config.enums import Roles
from . import Base


class UserRole(Base):

    __tablename__ = "user_role"

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey(Users.id), nullable=False)
    role = Column(Enum(Roles))
    role_id = Column(BigInteger)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
