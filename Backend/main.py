from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from pymongo import MongoClient

app=FastAPI()

class VehiclesIn(BaseModel):
    vehicle_brand:str
    model:str
    vehicle_number:str
    cost_per_hour:float
    is_available:bool
    
class VehiclesOut(BaseModel):
    vehicle_id:str
    rent_hours:str
    
client=MongoClient("mongodb://localhost:27017/")
AI_vehicles=client["Ai_vehicles_db"]
vehicles=AI_vehicles["vehicles"] 

@app.get("/")
async def welcome():
    return{
        "welecome Ai vehicle rental system"
    }   
        
    