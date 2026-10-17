import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# 1. Otwarcie pliku .env i załadowanie zmiennych do pamięci
load_dotenv()

# 2. Odczytanie linku do bazy danych
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# 3. Utworzenie głównego "silnika" bazy danych
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 4. Konfiguracja sesji (czyli pojedynczego połączenia z bazą)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Klasa bazowa, po której będą dziedziczyć wszystkie tabele w systemie (modele)
Base = declarative_base()

# 6. Zależność zarządzająca otwieraniem i zamykaniem połączenia dla zapytań API
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()