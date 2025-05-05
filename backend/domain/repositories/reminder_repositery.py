# backend/domain/repositories/reminder_repository.py
from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.reminder import Reminder
from domain.repositories.reminder_repository import ReminderRepository
from domain.entities.reminder import Reminder
from infrastructure.database.models import ReminderModel


class SQLAlchemyReminderRepository(ReminderRepository):
    def __init__(self, session):
        self.session = session
        
    def add(self, reminder: Reminder) -> Reminder:
        # Implementation here
        pass



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

