from sqlalchemy import select

from sqlalchemy.orm import Session
from schemas import EmployeeCreate,EmployeeResponse,EmployeeUpdate,EmployeeUpdateAll
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from models import Employee
from exceptions import EmployeeNotFoundError,DuplicateEmailError,DabaseOperationError

def create_employee(db:Session,data:EmployeeCreate)->Employee:
    employee = Employee(**data.model_dump())
    try:
        db.add(employee)
        db.commit()
        db.refresh(employee)
        return employee
    except IntegrityError as exc:
        db.rollback()
        raise DuplicateEmailError() from exc
    except SQLAlchemyError as exc:
        db.rollback()
        raise DabaseOperationError() from exc

def get_employee_by_id(db:Session,employee_id:int):
    employee = db.get(Employee, employee_id)
    if employee is None:
            raise EmployeeNotFoundError(employee_id)
    
    return employee

def get_employees(db: Session,skip: int = 0,limit: int = 100,) -> list[Employee]:
    statement = (select(Employee).order_by(Employee.id).offset(skip).limit(limit))
    return list(db.scalars(statement).all())

def update_employee(db: Session,employee_id: int,data: EmployeeUpdate,) -> Employee:
    employee = get_employee_by_id(db, employee_id)
    changes = data.model_dump(exclude_unset=True)

    if not changes:
        return employee

    if any(value is None for value in changes.values()):
        raise ValueError("Update fields cannot be null")

    for field, value in changes.items():
        setattr(employee, field, value)

    try:
        db.commit()
        db.refresh(employee)
        return employee

    except IntegrityError as exc:
        db.rollback()
        raise DuplicateEmailError() from exc

    except SQLAlchemyError as exc:
        db.rollback()
        raise DabaseOperationError() from exc



def update_employee_fields(db: Session,employee_id: int,data: EmployeeUpdateAll,) -> Employee:
    employee = get_employee_by_id(db, employee_id)

    try:
        employee.name = data.name
        employee.department = data.department
        employee.email=data.email
        employee.salary=data.salary

        db.commit()
        db.refresh(employee)

        return employee

    except SQLAlchemyError as exc:
        db.rollback()
        raise DabaseOperationError() from exc


def delete_employee(db: Session, id: int) -> None:
    employee = get_employee_by_id(db, id)

    try:
        db.delete(employee)
        db.commit()

    except SQLAlchemyError as exc:
        db.rollback()
        raise DabaseOperationError() from exc

    
    
    
    


     
    
    




