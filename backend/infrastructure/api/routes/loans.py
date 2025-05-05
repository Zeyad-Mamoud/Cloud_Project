from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import date
from application.use_cases.add_loan import AddLoanUseCase
from application.use_cases.update_loan import UpdateLoanUseCase
from infrastructure.database.db import get_loan_repository
from domain.entities.loan import Loan

router = APIRouter(prefix="/loans", tags=["loans"])

class LoanCreate(BaseModel):
    amount: float
    due_date: date
    loan_type: str
    contact_id: int

@router.post("/", response_model=Loan)
def create_loan(loan: LoanCreate, repo=Depends(get_loan_repository)):
    use_case = AddLoanUseCase(repo)
    return use_case.execute(loan.amount, loan.due_date, loan.loan_type, loan.contact_id)

@router.put("/{loan_id}")
def update_loan(loan_id: int, paid_amount: float = None, mark_as_paid: bool = False, repo=Depends(get_loan_repository)):
    use_case = UpdateLoanUseCase(repo)
    return use_case.execute(loan_id, paid_amount, mark_as_paid)