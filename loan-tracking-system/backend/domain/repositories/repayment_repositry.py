from abc import ABC, abstractmethod
from typing import List
from domain.entities.repayment import Repayment
from infrastructure.database.db import SessionLocal

# Repayment repository
class RepaymentRepository:

    def __init__(self):
        self.db = SessionLocal()

    def get_all_repayments(self):
        return self.db.query(Repayment).all()

    def get_repayment_by_id(self, repayment_id: int):
        return self.db.query(Repayment).filter(Repayment.id == repayment_id).first()

    def add_repayment(self, repayment: Repayment):
        self.db.add(repayment)
        self.db.commit()
        self.db.refresh(repayment)
        return repayment

    def update_repayment(self, repayment_id: int, updated_data: dict):
        repayment = self.get_repayment_by_id(repayment_id)
        for key, value in updated_data.items():
            setattr(repayment, key, value)
        self.db.commit()
        return repayment

    def delete_repayment(self, repayment_id: int):
        repayment = self.get_repayment_by_id(repayment_id)
        self.db.delete(repayment)
        self.db.commit()
