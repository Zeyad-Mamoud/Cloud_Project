from domain.entities.loan import Loan, LoanType, LoanStatus
from domain.repositories.loan_repository import LoanRepository
from datetime import date

class AddLoanUseCase:
    def __init__(self, loan_repository: LoanRepository):
        self.loan_repository = loan_repository

    def execute(self, amount: float, due_date: date, loan_type: str, contact_id: int) -> Loan:
        loan = Loan(
            id=None,
            amount=amount,
            due_date=due_date,
            loan_type=LoanType(loan_type),
            contact_id=contact_id,
            status=LoanStatus.ACTIVE,
            remaining_balance=amount
        )
        return self.loan_repository.add(loan)