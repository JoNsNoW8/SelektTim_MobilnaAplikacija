from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.models.korisnik import Korisnik
from app.core.security import verify_password, create_access_token

#Login endpoint

router = APIRouter(prefix="/auth", tags=["auth"])

def get_db(): 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    korisnik = db.query(Korisnik).filter(Korisnik.korisnickoIme == username).first()
    if not korisnik or not verify_password(password, korisnik.password_hash):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": korisnik.korisnickoIme, "Uloga": korisnik.Uloga})
    return {"access_token": token, "Uloga": korisnik.Uloga}