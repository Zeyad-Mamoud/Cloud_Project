from sqlalchemy import Column, Integer, Float, Date, String, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from domain.entities.loan import LoanType, LoanStatus
from domain.entities.reminder import ReminderStatus
from datetime import datetime
from .base import Base

class ContactModel(Base):
    __tablename__ = 'contacts'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    loans = relationship("LoanModel", back_populates="contact")

class LoanModel(Base):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True)
    contact_id = Column(Integer, ForeignKey("contacts.id"), nullable=False)
    amount = Column(Float, nullable=False)
    loan_type = Column(Enum(LoanType), nullable=False)
    description = Column(String)
    due_date = Column(Date, nullable=False)
    status = Column(Enum(LoanStatus), nullable=False, default=LoanStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    contact = relationship("Contact", back_populates="loans")
    reminders = relationship("ReminderModel", back_populates="loan")
    repayments = relationship("RepaymentModel", back_populates="loan")

class ReminderModel(Base):
    __tablename__ = "reminders"
    id = Column(Integer, primary_key=True)
    loan_id = Column(Integer, ForeignKey("loans.id"), nullable=False)
    remind_date = Column(Date, nullable=False)
    status = Column(Enum(ReminderStatus), nullable=False, default=ReminderStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    loan = relationship("LoanModel", back_populates="reminders")

class RepaymentModel(Base):
    __tablename__ = "repayments"
    id = Column(Integer, primary_key=True)
    loan_id = Column(Integer, ForeignKey("loans.id"), nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(Date, nullable=False)
    notes = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    loan = relationship("LoanModel", back_populates="repayments")