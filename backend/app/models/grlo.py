from sqlalchemy import Column, Integer, String, Date
from app.database.base import Base

class Grlo(Base):
    __tablename__ = "Grlo"

    ID_Grla = Column(Integer, primary_key=True)
    ID_Majke = Column(Integer)
    Kvalitet_mleka = Column(String(50))
    Datum_osemenjavanja = Column(Date)
    Datum_teljenja = Column(Date)
    Datum_rodjenja = Column(Date)
