from domain.entities.loan import Loan
from typing import List

class GetUpcomingLoansUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, days: int = 7) -> List[Loan]:
        return self.repository.get_upcoming_loans(days)