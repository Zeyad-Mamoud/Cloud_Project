from domain.entities.repayment import Repayment
from domain.repositories.repayment_repositry import RepaymentRepository
from datetime import datetime


class AddRepaymentUseCase:
    def __init__(self, repayment_repo: RepaymentRepository):
        self.repayment_repo = repayment_repo

    def execute(self, loan_id: int, amount: float, payment_date: datetime = None):
        payment_date = payment_date or datetime.utcnow()
        repayment = Repayment(
            loan_id=loan_id,
            amount=amount,
            payment_date=payment_date
        )
        return self.repayment_repo.add_repayment(repayment)
    

