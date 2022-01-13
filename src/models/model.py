from sqlalchemy import Column, String, TIMESTAMP, text, JSON
from sqlalchemy.dialects.mysql import INTEGER

from . import Base


class Student(Base):

    __tablename__ = "student"

    id = Column(INTEGER(11), primary_key=True)
    enroll = Column(INTEGER(11))
    personal_info = Column(JSON)
    name = Column(String(255))
    created_on = Column(
        TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
