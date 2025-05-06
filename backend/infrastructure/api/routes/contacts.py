from fastapi import APIRouter, Depends
from pydantic import BaseModel
from infrastructure.database.db import get_contact_repository
from domain.entities.contact import Contact
from application.use_cases.add_contact import AddContactUseCase
from application.use_cases.list_contacts import ListContactsUseCase


router = APIRouter()

class ContactCreate(BaseModel):
    name: str
    phone: str | None = None
    email: str | None = None

@router.post("/", response_model=Contact)
def create_contact(contact: ContactCreate, repo=Depends(get_contact_repository)):
    contact_entity = Contact(id=None, name=contact.name, phone=contact.phone, email=contact.email)
    use_case = AddContactUseCase(repo)
    return use_case.execute(contact_entity)


@router.get("/", response_model=list[Contact])
def list_contacts(repo=Depends(get_contact_repository)):
    use_case = ListContactsUseCase(repo)
    return use_case.execute()


