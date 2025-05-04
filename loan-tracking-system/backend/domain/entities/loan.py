from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from typing import Optional

class LoanType(Enum):
    BORROWED = "borrowed"
    LENT = "lent"

class LoanStatus(Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    PARTIALLY_PAID = "PARTIALLY_PAID"
    OVERDUE = "OVERDUE"

@dataclass
class Loan:
    id: Optional[int]
    user_id: int
    contact_id: int
    amount: float
    currency: str = "USD"
    loan_type: LoanType
    description: Optional[str]
    due_date: date
    status: LoanStatus = LoanStatus.PENDING
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None