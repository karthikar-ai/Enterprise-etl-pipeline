from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CustomerDB(Base):
    __tablename__ = "customers"

    customer_id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)
    created_at = Column(DateTime)