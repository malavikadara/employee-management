from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse

class EmployeeNotFoundError(Exception):
    def __init__(self,employee_id:int):
        self.employee_id = employee_id


class DuplicateEmailError(Exception):
    pass

class DabaseOperationError(Exception):
    pass

def register_exception_handlers(app:FastAPI):

    @app.exception_handler(EmployeeNotFoundError)
    async def employee_not_found(
        request: Request,
        exc: EmployeeNotFoundError,
    ):
        return JSONResponse(
            status_code=404,
            content={
                "detail": f"Employee {exc.employee_id} not found"
            },
        )

    @app.exception_handler(DuplicateEmailError)
    async def duplicate_email_error(
        request:Request,
        exc:DuplicateEmailError
    ):
        return JSONResponse(
            status_code=409,
            content={"detail": f"Email of this employee already exists"}
        )

    @app.exception_handler(DabaseOperationError)
    async def database_operations(
        request:Request,
        exc:DabaseOperationError
    ):
        return JSONResponse(
            status_code=500,
            context={"detail":f"Database operations failes"}
        )
        


    