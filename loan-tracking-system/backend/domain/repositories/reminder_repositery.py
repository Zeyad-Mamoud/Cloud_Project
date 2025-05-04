from abc import ABC, abstractmethod
from typing import List
from domain.entities.reminder import Reminder
from infrastructure.database.db import SessionLocal

# Reminder repository
class ReminderRepository:

    def __init__(self):
        self.db = SessionLocal()

    def get_all_reminders(self):
        return self.db.query(Reminder).all()

    def get_reminder_by_id(self, reminder_id: int):
        return self.db.query(Reminder).filter(Reminder.id == reminder_id).first()

    def add_reminder(self, reminder: Reminder):
        self.db.add(reminder)
        self.db.commit()
        self.db.refresh(reminder)
        return reminder

    def update_reminder(self, reminder_id: int, updated_data: dict):
        reminder = self.get_reminder_by_id(reminder_id)
        for key, value in updated_data.items():
            setattr(reminder, key, value)
        self.db.commit()
        return reminder

    def delete_reminder(self, reminder_id: int):
        reminder = self.get_reminder_by_id(reminder_id)
        self.db.delete(reminder)
        self.db.commit()

