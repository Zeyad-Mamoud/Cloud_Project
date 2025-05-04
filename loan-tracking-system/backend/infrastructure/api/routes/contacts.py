from fastapi import APIRouter, Depends
from pydantic import BaseModel
from infrastructure.database.db import get_contact_repository
from domain.entities.contact import Contact
from typing import Optional

router = APIRouter()

class ContactCreate(BaseModel):
    name: str
    phone: Optional[str]
    email: Optional[str]

@router.post("/", response_model=Contact)
def create_contact(contact: ContactCreate, repo=Depends(get_contact_repository)):
    contact_entity = Contact(id=None, name=contact.name, phone=contact.phone, email=contact.email)
    return repo.add(contact_entity)
