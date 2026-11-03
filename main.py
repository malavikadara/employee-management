from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from database import Base, engine
from exceptions import register_exception_handlers
from router.routers import router as employee_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Development only: create tables that do not exist.
    Base.metadata.create_all(bind=engine)
    yield
    engine.dispose()


app = FastAPI(
    title="Employee Management API",
    description="CRUD API using FastAPI and PostgreSQL",
    version="1.0.0",
    lifespan=lifespan,
)

register_exception_handlers(app)

app.include_router(employee_router)


@app.get("/")
def home():
    return {"message": "Employee Management API is running"}


@app.get("/health")
def health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {"status": "healthy", "database": "connected"}

    except SQLAlchemyError as exc:
        raise HTTPException(
            status_code=503,
            detail="Database is unavailable",
        ) from exc