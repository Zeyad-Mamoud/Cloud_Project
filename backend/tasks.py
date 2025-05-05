from celery import Celery
from infrastructure.database.db import LoanRepository
from datetime import datetime, timedelta
import os

app = Celery('tasks', broker='redis://redis:6379/0')

@app.task
def check_reminders():
    repo = LoanRepository()
    loans = repo.get_all()
    today = datetime.utcnow().date()
    for loan in loans:
        due_date = datetime.strptime(loan.due_date, '%Y-%m-%d').date()
        if due_date - today <= timedelta(days=3) and loan.status != 'paid':
            print(f"Reminder: Loan ID {loan.id} is due on {loan.due_date}! Amount: {loan.amount}, Remaining: {loan.remaining_balance}")