from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Order(BaseModel):
    id: Optional[int]
    client: str
    sku: str
    quantity: int
    unit: str
    time: Optional[datetime]
    state: Optional[bool]

    