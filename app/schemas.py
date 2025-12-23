from pydantic import BaseModel,Field
from typing import List

class HouseInput(BaseModel):
    area:int =Field(...,ge=0)
    bedrooms:int = Field(...,ge=0)
    bathrooms:int=Field(...,ge=0)
    stories:int=Field(...,ge=0)
    mainroad:str
    guestroom:str
    basement:str
    hotwaterheating:str
    airconditioning:str
    parking:int=Field(...,ge=0)
    prefarea:str
    furnishingstatus:str

class HouseOutput(BaseModel):
    result:float