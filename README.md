# Blog API

A simple blog API built with FastAPI that includes fake data generation.

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
venv\Scripts\activate  # Since you're on Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Run the application using:
```bash
python main.py
```

The API will be available at http://127.0.0.1:8000

## API Endpoints

- GET `/`: Welcome message
- GET `/posts`: List all blog posts
- GET `/posts/{post_id}`: Get a specific post
- GET `/users`: List all users

## API Documentation

Once the application is running, you can access:
- Interactive API documentation at http://127.0.0.1:8000/docs
- Alternative API documentation at http://127.0.0.1:8000/redoc 