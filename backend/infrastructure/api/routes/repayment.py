from fastapi import APIRouter, Depends
from pydantic import BaseModel
from infrastructure.database.db import get_repayment_repository
from domain.entities.repayment import Repayment

router = APIRouter()
