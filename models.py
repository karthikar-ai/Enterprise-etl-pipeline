from pydantic import BaseModel
from datetime import datetime


class Customer(BaseModel):
    customer_id: str
    name: str
    email: str
    created_at: datetime