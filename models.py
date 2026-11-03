
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import Integer,String,Float
from database import Base

class Employee(Base):
    __tablename__="employee"

    id:Mapped[int]= mapped_column(Integer,primary_key=True,index=True)
    name:Mapped[str]=mapped_column(String(100),nullable=False)
    email:Mapped[str]=mapped_column(String(255),nullable=False,unique=True,index=True)
    salary:Mapped[float]=mapped_column(Float,nullable=False)
    department:Mapped[str]=mapped_column(String(255),nullable=False)


