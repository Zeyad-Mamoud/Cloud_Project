from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import date
from application.use_cases.add_loan import AddLoanUseCase
from application.use_cases.update_loan import UpdateLoanUseCase
from infrastructure.database.db import get_loan_repository
from domain.entities.loan import Loan
