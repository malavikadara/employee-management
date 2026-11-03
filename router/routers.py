from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from schemas import EmployeeResponse,EmployeeCreate,EmployeeUpdate,EmployeeUpdateAll
from sqlalchemy.orm import Session
from database import get_db
from services import employee_service 


router=APIRouter(prefix="/employee",tags=["Employee"])

@router.post("/",response_model=EmployeeResponse,status_code=status.HTTP_201_CREATED)
def create_employee(data:EmployeeCreate,db:Session=Depends(get_db)):
    return employee_service.create_employee(db,data)


@router.get("/",response_model=list[EmployeeResponse])
def getEmployees(db:Session=Depends(get_db),skip: int = Query(default=0, ge=0),limit: int = Query(default=100, ge=1, le=100),):
    return employee_service.get_employees(db,skip,limit)

@router.get("/{employeeid}",response_model=EmployeeResponse)
def getEmployeeById(employeeid: int,db:Session=Depends(get_db),):
    return employee_service.get_employee_by_id(db,employeeid)

@router.patch("/{employeeid}",response_model=EmployeeResponse,)
def updateEmployee(employeeid:int,data:EmployeeUpdate,db:Session=Depends(get_db)):
    try:
        return employee_service.update_employee(db, employeeid, data)
    except ValueError as exc:
        raise HTTPException(status_code=422,detail=str(exc), ) from exc

@router.put("/{employeeid}",response_model=EmployeeResponse,status_code=status.HTTP_200_OK,)
def updateEmployee(employeeid: int,data: EmployeeUpdateAll,db: Session = Depends(get_db),):
    return employee_service.update_employee(db, employeeid, data)




@router.delete("/{employeeid}",status_code=status.HTTP_204_NO_CONTENT,)
def deleteEmployee(employeeid:int,db:Session=Depends(get_db),):
    employee_service.delete_employee(db,employeeid)
    return Response(status_code=status.HTTP_204_NO_CONTENT)







