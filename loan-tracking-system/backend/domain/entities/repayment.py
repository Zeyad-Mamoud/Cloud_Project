from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional

@dataclass
class Repayment:
    id: Optional[int]
    loan_id: int
    amount: float
    payment_date: date
    notes: Optional[str] = None
    created_at: Optional[datetime] = None
