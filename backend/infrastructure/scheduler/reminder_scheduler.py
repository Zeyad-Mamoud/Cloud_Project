from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from infrastructure.database.db import get_db
from sqlalchemy.orm import Session
from domain.entities.loan import LoanStatus
import logging
from domain.entities.loan import Loan


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_reminders():
    db: Session = next(get_db())
    today = datetime.now().date()
    upcoming_threshold = today + timedelta(days=7)  # تذكير قبل 7 أيام

    loans = db.query(Loan).filter(Loan.status != LoanStatus.PAID).all()
    for loan in loans:
        due_date = datetime.fromisoformat(loan.due_date).date()
        if today <= due_date <= upcoming_threshold:
            logger.info(f"Reminder: Loan {loan.id} due on {loan.due_date} (Amount: {loan.remaining_balance})")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_reminders, 'interval', days=1)
    scheduler.start()
    logger.info("Scheduler started for loan reminders.")

if __name__ == "__main__":
    start_scheduler()