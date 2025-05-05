# backend/domain/repositories/repayment_repository.py
from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.repayment import Repayment

class RepaymentRepository(ABC):

    @abstractmethod
    def add(self, repayment: Repayment) -> Repayment:
        pass

    @abstractmethod
    def get_by_id(self, repayment_id: int) -> Optional[Repayment]:
        pass

    @abstractmethod
    def get_all(self) -> List[Repayment]:
        pass

    @abstractmethod
    def get_by_loan_id(self, loan_id: int) -> List[Repayment]:
        pass

    @abstractmethod
    def get_total_paid_amount(self, loan_id: int) -> float:
        pass