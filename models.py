from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Configuration(BaseModel):
    id: int
    country_code: str
    business_name: str
    pan: str
    gstin: str


