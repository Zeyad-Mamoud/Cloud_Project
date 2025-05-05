from fastapi import APIRouter, Depends
from pydantic import BaseModel
from infrastructure.database.db import get_repayment_repository
from domain.entities.repayment import Repayment

router = APIRouter(prefix="/repayment", tags=["repayment"])

class RepaymentCreate(BaseModel):
    loan_id: int
    amount: float
    date: str  # Assuming date is a string in 'YYYY-MM-DD' format


