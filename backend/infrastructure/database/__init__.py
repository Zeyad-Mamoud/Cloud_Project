from .base import Base, engine
from .models import *  # Import all models

def init_db():
    Base.metadata.create_all(engine)