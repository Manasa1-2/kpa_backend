# Tracker API

This project is a backend service developed using **FastAPI** and **PostgreSQL**, designed to handle user activity tracking via webhook requests. It allows recording, retrieving, and managing user activities for a given platform.

## 🚀 Features

- RESTful APIs with FastAPI
- PostgreSQL integration using SQLAlchemy
- Swagger UI documentation (`/docs`)
- Automatic validation and error handling
- Foreign key constraints between user and activity tables

## 📂 Project Structure

webhook_activity/
│
├── app.py # Main FastAPI application
├── models.py # SQLAlchemy models
├── db.py # Database connection setup
├── action_repo/ # Database operations layer
├── static/ # CSS files
├── templates/ # HTML templates
├── requirements.txt # Dependencies


- Create Virtual Environment

python -m venv venv
venv/bin/activate 

- Install Requirements
pip install -r requirements.txt

- Run the App
uvicorn app:app --reload
