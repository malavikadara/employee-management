from pydantic import BaseModel,Field,EmailStr,ConfigDict

class EmployeeCreate(BaseModel):
    name:str=Field(min_length=2, max_length=100)
    email:EmailStr
    salary:float=Field(gt=0)
    department:str=Field(min_length=2, max_length=100)


class EmployeeUpdate(BaseModel):
    name:str|None=Field(default=None,min_length=2, max_length=100)
    email:None=None
    salary:float|None=Field(default=None,gt=0)
    department:str|None=Field(default=None,min_length=2, max_length=100)

class EmployeeUpdateAll(BaseModel):
    name:str=Field(min_length=2, max_length=100)
    email:EmailStr
    salary:float=Field(gt=0)
    department:str=Field(min_length=2, max_length=100)

class EmployeeResponse(BaseModel):
    id:int
    name:str
    email:EmailStr
    department:str
    salary:float

    model_config = ConfigDict(from_attributes=True)


