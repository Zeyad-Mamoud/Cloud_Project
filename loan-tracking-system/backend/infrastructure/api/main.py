from fastapi import FastAPI
from infrastructure.api.routes import loans, contacts
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Loan Tracking System")

# Add middleware to handle trailing slashes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(loans.router, prefix="/loans", tags=["loans"])
app.include_router(contacts.router, prefix="/contacts", tags=["contacts"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Loan Tracking System"}
