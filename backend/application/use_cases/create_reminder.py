from domain.entities.reminder import Reminder
from domain.repositories.reminder_repositery import ReminderRepository
from datetime import datetime

class CreateReminderUseCase:
    def __init__(self, reminder_repo: ReminderRepository):
        self.reminder_repo = reminder_repo

    def execute(self, loan_id: int, message: str, remind_at: datetime):
        reminder = Reminder(
            loan_id=loan_id,
            message=message,
            remind_at=remind_at
        )
        return self.reminder_repo.add_reminder(reminder)
