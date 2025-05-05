from dataclasses import dataclass
from typing import Optional
from datetime import date, datetime
from enum import Enum

class ReminderStatus(Enum):
    PENDING = "PENDING"
    SENT = "SENT"
    FAILED = "FAILED"


@dataclass
class Reminder:
    id: Optional[int]
    loan_id: int
    remind_date: date
    status: ReminderStatus = ReminderStatus.PENDING
    created_at: Optional[datetime] = None