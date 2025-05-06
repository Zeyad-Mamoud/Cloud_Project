from domain.entities.contact import Contact
from domain.repositories.contact_repository import ContactRepository

class AddContactUseCase:
    def __init__(self, repository: ContactRepository):
        self.repository = repository

    def execute(self, contact: Contact):
        self.repository.add(contact)