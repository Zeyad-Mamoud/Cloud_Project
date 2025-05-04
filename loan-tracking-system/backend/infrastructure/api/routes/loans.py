from fastapi import APIRouter, Depends
from pydantic import BaseModel
from infrastructure.database.db import get_loan_repository
from domain.entities.loan import LoanType, Loan
from application.use_cases.add_loan import AddLoanUseCase
from datetime import datetime
from fastapi import HTTPException

router = APIRouter()

class LoanCreate(BaseModel):
    amount: float
    due_date: str  
    loan_type: LoanType
    contact_id: int

@router.post("/", response_model=Loan)
def create_loan(loan: LoanCreate, repo=Depends(get_loan_repository)):
    try:
        use_case = AddLoanUseCase(repo)
        due_date = datetime.strptime(loan.due_date, "%Y-%m-%d").date()
        return use_case.execute(
            amount=loan.amount,
            due_date=due_date,
            loan_type=loan.loan_type.value,
            contact_id=loan.contact_id
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
