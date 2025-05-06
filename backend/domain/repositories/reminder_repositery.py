from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.reminder import Reminder
from infrastructure.database.session import SessionLocal
from datetime import datetime

class ReminderRepository(ABC):

    @abstractmethod
    def add(self, reminder: Reminder) -> Reminder:
        pass

    @abstractmethod
    def get_by_id(self, reminder_id: int) -> Optional[Reminder]:
        pass

    @abstractmethod
    def get_all(self) -> List[Reminder]:
        pass

    @abstractmethod
    def get_pending_reminders(self) -> List[Reminder]:
        pass

    @abstractmethod
    def update_status(self, reminder_id: int, status: str) -> None:
        pass

