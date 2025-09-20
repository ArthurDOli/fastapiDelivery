# FastAPI Delivery API

The FastAPI Delivery API is a REST API developed in Python with FastAPI, designed to manage an ordering system. The application serves as a complete backend for a delivery or e-commerce platform, including user authentication, permission management, and a full workflow for creating and handling orders.

## Features

- **Secure Authentication with JWT:** A complete system for account creation, login, and logout using JWT to protect routes. It includes access and refresh tokens.
- **Role-Based Access Control:** A clear distinction between regular users and administrators. Critical routes, such as listing all orders, are restricted to administrators.
- **Complete Order Management:** CRUD (Create, Read, Update, Delete) operations for orders, allowing users to create, cancel, finalize, and view orders.
- **Item Handling:** Add and remove items from an existing order, with automatic calculation of the total price.
- **Data Validation:** Uses Pydantic to define data schemas, ensuring that all API requests and responses are consistent and valid.

## Technologies Used

- **Backend:** Python, FastAPI
- **Database:** SQLite, SQLAlchemy

## Installation and Setup

Follow the steps below to set up and run the project locally:

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/ArthurDOli/fastapiDelivery.git](https://github.com/ArthurDOli/fastapiDelivery.git)
    cd fastapiDelivery
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv .venv
    # On Windows
    .venv\Scripts\activate
    # On macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install the dependencies:**
    Install the dependencies with:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the project root and add the following variables. You can generate a strong secret key for `SECRET_KEY`.

    ```
    SECRET_KEY=your_super_secret_key
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

5.  **Create and update the database with Alembic:**
    This command will read the migration files and create the `banco.db` file with all the necessary tables.

    ```bash
    alembic upgrade head
    ```

6.  **Run the application:**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`, and the interactive documentation at `http://127.0.0.1:8000/docs`.

## Project Structure

```bash
fastapiDelivery/
├── alembic/
│   └── ...
├── .gitignore
├── alembic.ini
├── auth_routes.py
├── dependencies.py
├── main.py
├── models.py
├── order_routes.py
├── schemas.py
├── security.py
└── README.md
```
