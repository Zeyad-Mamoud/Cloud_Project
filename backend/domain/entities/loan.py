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
    id: Optional[int] = None
    user_id: int
    contact_id: int
    amount: float
    loan_type: LoanType  # Moved before default arguments
    due_date: date
    currency: str = "USD"  # Default argument
    description: Optional[str] = None  # Default argument
    status: LoanStatus = LoanStatus.PENDING  # Default argument
    created_at: Optional[datetime] = None  # Default argument
    updated_at: Optional[datetime] = None  # Default argument