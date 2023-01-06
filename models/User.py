from sqlalchemy import Boolean, Column, Integer, String, Date
from sqlalchemy.orm import relationship

import uuid

from config.database import Base


class User(Base):

    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    birth_date = Column(Date, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)