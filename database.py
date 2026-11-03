from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase


db_url="postgresql+psycopg://{username}:{password}@localhost:5432/employee"
engine=create_engine(db_url)
session = sessionmaker(bind=engine,expire_on_commit=False, autoflush=False)
class Base(DeclarativeBase):
    pass
def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()


















