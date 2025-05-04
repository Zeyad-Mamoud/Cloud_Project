# <xaiArtifact artifact_id="f6fc2ae8-7c6e-47e3-99b7-6d767f725cee" 
# artifact_version_id="f1f2544b-219c-45d0-a3cb-4969f654d5da"
# title="models.py" contentType="text/python">
from sqlalchemy import Column, Integer, Float, Date, String, Enum, ForeignKey
from sqlalchemy.orm import declarative_base
from domain.entities.loan import LoanType, LoanStatus

Base = declarative_base()

class LoanModel(Base):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    due_date = Column(Date, nullable=False)
    loan_type = Column(Enum(LoanType), nullable=False)
    contact_id = Column(Integer, ForeignKey("contacts.id"), nullable=False)
    status = Column(Enum(LoanStatus), nullable=False)
    remaining_balance = Column(Float, nullable=False)

class ContactModel(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String)
    email = Column(String)