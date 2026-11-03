# Employee Management System

Full-stack Employee Management application built using FastAPI, Python, SQLAlchemy, PostgreSQL, and React.

## Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL
- Pydantic

### Frontend
- React
- JavaScript
- npm

## Project Structure

```text
employee_FastApi/
├── frontend/          # React application
├── router/            # API routes
├── services/          # Business logic
├── database.py        # Database connection
├── exceptions.py      # Custom exception handling
├── main.py            # FastAPI application entry point
├── models.py          # SQLAlchemy models
├── schemas.py         # Pydantic schemas
├── requirements.txt   # Python dependencies
├── .gitignore
└── README.md
```

## Backend Setup

### 1. Clone Repository

```bash
git clone https://github.com/USERNAME/employee_FastApi.git
cd employee_FastApi
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
```

### 3. Activate Virtual Environment

Mac/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Configure PostgreSQL

Create a PostgreSQL database named `employee`.

Configure the database connection in your `.env` file:

```env
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/employee
```

### 6. Run FastAPI Application

```bash
uvicorn main:app --reload
```

Backend URL:

http://127.0.0.1:8000

### 7. API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc

## Frontend Setup

Open a new terminal.

### 1. Navigate to Frontend

```bash
cd frontend
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Start React Application

```bash
npm run dev
```

Open the frontend URL displayed in your terminal.

## Running the Complete Application

Run the backend and frontend in two separate terminals.

**Terminal 1 – FastAPI**

```bash
source .venv/bin/activate
uvicorn main:app --reload
```

**Terminal 2 – React**

```bash
cd frontend
npm run dev
```

## Git Commands

```bash
git add .
git commit -m "Update employee management application"
git push origin main
```

## Features

- Employee CRUD operations
- REST API development
- PostgreSQL database integration
- SQLAlchemy ORM
- Custom exception handling
- Pydantic request validation
- React frontend integration
- Interactive Swagger API documentation
