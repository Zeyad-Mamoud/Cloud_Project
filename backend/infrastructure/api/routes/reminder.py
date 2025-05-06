from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from datetime import date
from typing import Optional
# from application.use_cases.add_reminder import AddReminderUseCase
# from application.use_cases.update_reminder import UpdateReminderUseCase
# from application.use_cases.get_reminders import GetRemindersUseCase
from infrastructure.database.db import get_reminder_repository
from domain.entities.reminder import Reminder

router = APIRouter(prefix="/reminders", tags=["reminders"])

# class ReminderCreate(BaseModel):
#     loan_id: int
#     remind_date: date
#     message: Optional[str] = None

# class ReminderUpdate(BaseModel):
#     status: Optional[str] = None
#     remind_date: Optional[date] = None
#     message: Optional[str] = None

# @router.post("/", response_model=Reminder)
# def create_reminder(
#     reminder: ReminderCreate, 
#     repo=Depends(get_reminder_repository)
# ):
#     """Create a new reminder for a loan"""
#     use_case = AddReminderUseCase(repo)
#     return use_case.execute(
#         loan_id=reminder.loan_id,
#         remind_date=reminder.remind_date,
#         message=reminder.message
#     )

# @router.get("/", response_model=list[Reminder])
# def get_reminders(
#     loan_id: Optional[int] = None,
#     status: Optional[str] = None,
#     repo=Depends(get_reminder_repository)
# ):
#     """Get all reminders with optional filtering"""
#     use_case = GetRemindersUseCase(repo)
#     return use_case.execute(loan_id=loan_id, status=status)

# @router.get("/{reminder_id}", response_model=Reminder)
# def get_reminder(
#     reminder_id: int,
#     repo=Depends(get_reminder_repository)
# ):
#     """Get a specific reminder by ID"""
#     use_case = GetRemindersUseCase(repo)
#     reminder = use_case.get_by_id(reminder_id)
#     if not reminder:
#         raise HTTPException(status_code=404, detail="Reminder not found")
#     return reminder

# @router.put("/{reminder_id}", response_model=Reminder)
# def update_reminder(
#     reminder_id: int,
#     update_data: ReminderUpdate,
#     repo=Depends(get_reminder_repository)
# ):
#     """Update a reminder's status or details"""
#     use_case = UpdateReminderUseCase(repo)
#     return use_case.execute(
#         reminder_id=reminder_id,
#         status=update_data.status,
#         remind_date=update_data.remind_date,
#         message=update_data.message
#     )

# @router.delete("/{reminder_id}", status_code=204)
# def delete_reminder(
#     reminder_id: int,
#     repo=Depends(get_reminder_repository)
# ):
#     """Delete a reminder"""
#     success = repo.delete(reminder_id)
#     if not success:
#         raise HTTPException(status_code=404, detail="Reminder not found")
#     return None