from domain.entities.loan import Loan, LoanStatus
from domain.repositories.loan_repository import LoanRepository

class UpdateLoanUseCase:
    def __init__(self, loan_repository: LoanRepository):
        self.loan_repository = loan_repository

    def execute(self, loan_id: int, paid_amount: float = None, mark_as_paid: bool = False) -> Loan:
        loan = self.loan_repository.get_by_id(loan_id)
        if not loan:
            raise ValueError(f"Loan with id {loan_id} not found")

        if mark_as_paid:
            loan.status = LoanStatus.PAID
            loan.remaining_balance = 0
        elif paid_amount is not None:
            if paid_amount > loan.remaining_balance:
                raise ValueError("Paid amount exceeds remaining balance")
            loan.remaining_balance -= paid_amount
            loan.status = LoanStatus.PARTIALLY_PAID if loan.remaining_balance > 0 else LoanStatus.PAID

        return self.loan_repository.update(loan)
