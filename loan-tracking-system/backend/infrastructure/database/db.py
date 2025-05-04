from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain.repositories.loan_repository import LoanRepository
from domain.repositories.contact_repository import ContactRepository
from domain.entities.loan import Loan
from domain.entities.contact import Contact
from typing import List
from infrastructure.database.models import LoanModel, ContactModel

DATABASE_URL = "postgresql://user:password@db:5432/loan_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

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
                if key != "id" and value is not None:
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

def get_loan_repository():
    return SQLAlchemyLoanRepository()

def get_contact_repository():
    return SQLAlchemyContactRepository()
