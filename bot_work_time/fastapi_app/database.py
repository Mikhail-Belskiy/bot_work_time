from fastapi.security import OAuth2PasswordBearer
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

URL = (f"postgresql://"
       f"{config('POSTGRES_USER')}:"
       f"{config('POSTGRES_PASSWORD')}"
       f"@{config('POSTGRES_HOST')}/"
       f"{config('POSTGRES_DB')}")

engine = create_engine(URL)
SessionLocal=sessionmaker(bind=engine, expire_on_commit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")