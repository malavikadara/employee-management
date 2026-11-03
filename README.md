# Employee Management API – FastAPI

A RESTful Employee Management application built using Python, FastAPI, SQLAlchemy, and PostgreSQL.

## 1. Prerequisites

Install the following before running the application:

- Python 3.9+
- PostgreSQL
- pip
- Git
- VS Code (recommended)

Check Python version:

```bash
python3 --version
```

Check pip:

```bash
pip3 --version
```

## 2. Clone the Repository

```bash
git clone https://github.com/USERNAME/employee_FastApi.git
cd employee_FastApi
```

## 3. Create a Virtual Environment

Create an isolated Python environment:

```bash
python3 -m venv .venv
```

## 4. Activate the Virtual Environment

For macOS/Linux:

```bash
source .venv/bin/activate
```

For Windows:

```bash
.venv\Scripts\activate
```

After activation, you should see `(.venv)` in your terminal.

## 5. Install Dependencies

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

If requirements.txt is not available, install the main dependencies:

```bash
pip install fastapi uvicorn sqlalchemy psycopg python-dotenv
```

## 6. Configure Database

1. Install and start PostgreSQL.
2. Create a database named `employee`.
3. Configure your database connection string in the project's environment configuration.

Example:

```env
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/employee
```

Update the database username and password according to your local PostgreSQL configuration.

Do not commit your `.env` file to GitHub.

## 7. Run the FastAPI Application

Start the development server using Uvicorn:

```bash
uvicorn main:app --reload
```

If your application entry point is inside a package, adjust the module path accordingly.

Example:

```bash
uvicorn app.main:app --reload
```

The application will run at:

http://127.0.0.1:8000

## 8. Access Swagger API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc

Use Swagger UI to test Employee CRUD operations:

- Create Employee – POST
- Get All Employees – GET
- Get Employee By ID – GET
- Update Employee – PUT
- Delete Employee – DELETE

## 9. Running the UI (React Frontend)

If the project has a separate React frontend:

Open another terminal and navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the React development server:

```bash
npm run dev
```

The frontend will run at the URL displayed in your terminal (usually http://localhost:5173 for Vite).

Make sure the frontend API configuration points to the FastAPI backend.

## 10. Stop the Application

Press:

```bash
CTRL + C
```

Deactivate the virtual environment:

```bash
deactivate
```

## 11. Git Commands

Check modified files:

```bash
git status
```

Add changes:

```bash
git add .
```

Commit changes:

```bash
git commit -m "Add FastAPI employee management application"
```

Push changes to GitHub:

```bash
git push origin main
```

## Project Features

- FastAPI REST API
- Employee CRUD operations
- PostgreSQL database integration
- SQLAlchemy ORM
- Virtual environment management
- Exception handling
- Request validation using Pydantic
- Interactive Swagger documentation
