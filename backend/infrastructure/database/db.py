from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain.repositories.loan_repository import LoanRepository
from domain.repositories.contact_repository import ContactRepository
from domain.repositories.reminder_repositery import ReminderRepository
from domain.repositories.repayment_repositry import RepaymentRepository
from domain.entities.loan import Loan
from domain.entities.contact import Contact
from domain.entities.reminder import Reminder
from domain.entities.repayment import Repayment
from infrastructure.database.models import LoanModel, ContactModel, ReminderModel, RepaymentModel
from infrastructure.database.session import SessionLocal

from typing import List

# DATABASE_URL = "postgresql://postgres:0000@db:5432/loan_db"
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class SQLAlchemyLoanRepository(LoanRepository):
    def add(self, loan: Loan) -> Loan:
        with SessionLocal() as session:
            db_loan = LoanModel(**loan.__dict__)
            session.add(db_loan)
            session.commit()
            session.refresh(db_loan)
            return Loan(**db_loan.__dict__)

    def get_by_id(self, loan_id: int) -> Loan:
        with SessionLocal() as session:
            db_loan = session.query(LoanModel).filter(LoanModel.id == loan_id).first()
            return Loan(**db_loan.__dict__) if db_loan else None

    def get_all(self) -> List[Loan]:
        with SessionLocal() as session:
            db_loans = session.query(LoanModel).all()
            return [Loan(**loan.__dict__) for loan in db_loans]

    def update(self, loan: Loan) -> Loan:
        with SessionLocal() as session:
            db_loan = session.query(LoanModel).filter(LoanModel.id == loan.id).first()
            for key, value in loan.__dict__.items():
                setattr(db_loan, key, value)
            session.commit()
            session.refresh(db_loan)
            return Loan(**db_loan.__dict__)

class SQLAlchemyContactRepository(ContactRepository):
    def add(self, contact: Contact) -> Contact:
        with SessionLocal() as session:
            db_contact = ContactModel(**contact.__dict__)
            session.add(db_contact)
            session.commit()
            session.refresh(db_contact)
            return Contact(**db_contact.__dict__)

    def get_by_id(self, contact_id: int) -> Contact:
        with SessionLocal() as session:
            db_contact = session.query(ContactModel).filter(ContactModel.id == contact_id).first()
            return Contact(**db_contact.__dict__) if db_contact else None

    def get_all(self) -> List[Contact]:
        with SessionLocal() as session:
            db_contacts = session.query(ContactModel).all()
            return [Contact(**contact.__dict__) for contact in db_contacts]

class SQLAlchemyReminderRepository(ReminderRepository):
    def add(self, reminder: Reminder) -> Reminder:
        with SessionLocal() as session:
            db_reminder = ReminderModel(**reminder.__dict__)
            session.add(db_reminder)
            session.commit()
            session.refresh(db_reminder)
            return Reminder(**db_reminder.__dict__)

    def get_by_id(self, reminder_id: int) -> Reminder:
        with SessionLocal() as session:
            db_reminder = session.query(ReminderModel).filter(ReminderModel.id == reminder_id).first()
            return Reminder(**db_reminder.__dict__) if db_reminder else None

    def get_all(self) -> List[Reminder]:
        with SessionLocal() as session:
            db_reminders = session.query(ReminderModel).all()
            return [Reminder(**reminder.__dict__) for reminder in db_reminders]
        
class SQLAlchemyRepaymentRepository(RepaymentRepository):
    def add(self, repayment: Repayment) -> Repayment:
        with SessionLocal() as session:
            db_repayment = RepaymentModel(**repayment.__dict__)
            session.add(db_repayment)
            session.commit()
            session.refresh(db_repayment)
            return Repayment(**db_repayment.__dict__)

    def get_by_id(self, repayment_id: int) -> Repayment:
        with SessionLocal() as session:
            db_repayment = session.query(RepaymentModel).filter(RepaymentModel.id == repayment_id).first()
            return Repayment(**db_repayment.__dict__) if db_repayment else None

    def get_all(self) -> List[Repayment]:
        with SessionLocal() as session:
            db_repayments = session.query(RepaymentModel).all()
            return [Repayment(**repayment.__dict__) for repayment in db_repayments]

    def get_by_loan_id(self, loan_id: int) -> List[Repayment]:
        with SessionLocal() as session:
            db_repayments = session.query(RepaymentModel).filter(RepaymentModel.loan_id == loan_id).all()
            return [Repayment(**repayment.__dict__) for repayment in db_repayments]

    # def get_total_paid_amount(self, loan_id: int) -> float:
    #     with SessionLocal() as session:
    #         total_paid = session.query(func.sum(RepaymentModel.amount)).filter(RepaymentModel.loan_id == loan_id).scalar()
    #         return total_paid if total_paid else 0.0

def get_loan_repository():
    return SQLAlchemyLoanRepository()

def get_contact_repository():
    return SQLAlchemyContactRepository()

def get_repayment_repository():
    return SQLAlchemyRepaymentRepository()

def get_reminder_repository():
    return SQLAlchemyReminderRepository()