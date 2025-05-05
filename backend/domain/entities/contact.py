from dataclasses import dataclass
from typing import Optional
from datetime import datetime



@dataclass
class Contact:
    id: Optional[int]
    name: str
    email: Optional[str]
    phone: Optional[str]
    created_at: Optional[datetime] = None
    