from sqlalchemy import Column, Integer, Float, Date, String, Enum, ForeignKey
from sqlalchemy.orm import declarative_base
from domain.entities.loan import LoanType, LoanStatus
from domain.entities.reminder import ReminderStatus




Base = declarative_base()

class ContactModel(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String)
    email = Column(String)
    created_at = Column(Date, nullable=False)


class LoanModel(Base):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True)
    contact_id = Column(Integer, ForeignKey("contacts.id"), nullable=False)
    amount = Column(Float, nullable=False)
    loan_type = Column(Enum(LoanType), nullable=False)
    description = Column(String, nullable=False)
    due_date = Column(Date, nullable=False)
    status = Column(Enum(LoanStatus), nullable=False)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=False)
    
class ReminderModel(Base):
    __tablename__ = "reminders"
    id = Column(Integer, primary_key=True)
    loan_id = Column(Integer, ForeignKey("loans.id"), nullable=False)
    remind_date = Column(Date, nullable=False)
    status = Column(Enum(ReminderStatus), nullable=False)
    created_at = Column(Date, nullable=False)
    reminder_date = Column(Date, nullable=False)
    status = Column(Enum(ReminderStatus), nullable=False)
    created_at = Column(Date, nullable=False)  



class RepaymentModel(Base):
    __tablename__ = "repayments"
    id = Column(Integer, primary_key=True)
    loan_id = Column(Integer, ForeignKey("loans.id"), nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(Date, nullable=False)
    notes = Column(String, nullable=False)
    created_at = Column(Date, nullable=False)
    
   
