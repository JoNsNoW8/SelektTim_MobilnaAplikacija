from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  #Kontekst za heširanje lozinki koristeći bcrypt algoritam

def hash_password(password: str) -> str:
    return pwd_context.hash(password)  #Funkcija za heširanje lozinke

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)  #Funkcija za verifikaciju lozinke

SECRET_KEY = "CHANGE_ME"  #Tajni ključ za JWT token
ALGORITHM = "HS256"  #Algoritam za potpisivanje JWT tokena

def create_access_token(data: dict):
    expire = datetime.utcnow() + timedelta(hours=8)  #Postavljanje vremena isteka tokena na 8 sati
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM) #Funkcija za kreiranje JWT tokena