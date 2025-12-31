from fastapi import FastAPI
from app.routers import auth

app = FastAPI(title ="SelektTim API")

@app.get("/") #Root endpoint za proveravanje statusa API-ja
def root():
    return {"status" : "API is running"} #Root endpoint odgovor

app.include_router(auth.router) #Ukljucivanje auth router-a