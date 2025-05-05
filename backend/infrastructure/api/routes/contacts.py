from fastapi import APIRouter, Depends
from pydantic import BaseModel
from infrastructure.database.db import get_contact_repository
from domain.entities.contact import Contact
from sqlalchemy import Column, Integer, Float, Date, String, Enum, ForeignKey
from sqlalchemy.orm import declarative_base
from domain.entities.loan import LoanType, LoanStatus

router = APIRouter(prefix="/contacts", tags=["contacts"])

class ContactCreate(BaseModel):
    name: str
    phone: str | None
    email: str | None

@router.post("/", response_model=Contact)
def create_contact(contact: ContactCreate, repo=Depends(get_contact_repository)):
        contact_entity = Contact(id=None, name=contact.name, phone=contact.phone, email=contact.email)

    


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
    contact_entity = Contact(id=None, name=contact.name, phone=contact.phone, email=contact.email)
