from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional

class LoanType(Enum):
    BORROWED = "borrowed"
    LENT = "lent"

class LoanStatus(Enum):
    ACTIVE = "active"
    PAID = "paid"
    PARTIALLY_PAID = "partially_paid"

@dataclass
class Loan:
    id: Optional[int]
    amount: float
    due_date: date
    loan_type: LoanType
    contact_id: int
    status: LoanStatus
    remaining_balance: float