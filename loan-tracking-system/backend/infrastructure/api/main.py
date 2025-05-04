from fastapi import FastAPI
from infrastructure.api.routes import loans, contacts, repayment, reminder

app = FastAPI(title="Loan Tracking System")

app.include_router(loans.router, prefix="/loans", tags=["loans"])
app.include_router(contacts.router, prefix="/contacts", tags=["contacts"])
app.include_router(reminder.router, prefix="/reminder", tags=["reminder"])
app.include_router(reminder.repayment, prefix="/repayment", tags=["repayment"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Loan Tracking System"}
