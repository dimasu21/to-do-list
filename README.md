# Simple To-Do List API

A simple To-Do List application with a FastAPI backend and a modern HTML/JS frontend.

## Features

- **Backend**: Built with FastAPI for high performance and automatic documentation.
- **Frontend**: Single-page application using vanilla HTML, CSS, and JavaScript.
- **Design**: Modern dark mode interface with glassmorphism effects.
- **CRUD Operations**: Create, Read, Update, and Delete tasks.
- **In-Memory Storage**: Tasks are stored in memory (reset on server restart).

## Prerequisites

- Python 3.7+
- pip

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/dimasu21/to-do-list.git
    cd to-do-list
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Start the backend server:
    ```bash
    uvicorn main:app --reload
    ```

2.  Open the application:
    - **Frontend**: Open `index.html` in your web browser.
    - **API Documentation**: Go to `http://127.0.0.1:8000/docs` to view the Swagger UI.

## API Endpoints

- `GET /tasks`: Retrieve all tasks.
- `GET /tasks/{task_id}`: Retrieve a specific task.
- `POST /tasks`: Create a new task.
- `PUT /tasks/{task_id}`: Update an existing task.
- `DELETE /tasks/{task_id}`: Delete a task.

## Project Structure

- `main.py`: The FastAPI application and logic.
- `index.html`: The frontend user interface.
- `requirements.txt`: Python dependencies.
- `verify_api.py`: Script to verify API functionality.
