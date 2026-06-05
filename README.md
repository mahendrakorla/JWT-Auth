🚀 FastAPI Authentication System (JWT + SQLAlchemy + bcrypt)

A simple backend authentication system built using FastAPI, MySQL, SQLAlchemy, and JWT authentication. This project demonstrates user signup, login, password hashing, and basic CRUD operations.

📌 Features
User Signup with password hashing (bcrypt)
Secure Login with JWT token generation
Password verification
Retrieve all users
Delete user by username
MySQL database integration using SQLAlchemy ORM
Clean REST API structure
🛠️ Tech Stack
Python
FastAPI
SQLAlchemy
MySQL
Passlib (bcrypt)
JOSE (JWT)
📂 Project Structure
project/
│── main.py
│── requirements.txt
│── README.md
⚙️ Installation
1. Clone the repository
git clone https://github.com/your-username/fastapi-auth.git
cd fastapi-auth
2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install fastapi uvicorn sqlalchemy pymysql passlib[bcrypt] python-jose
🗄️ Database Setup (MySQL)

Create a database:

CREATE DATABASE dairy;

Update credentials in main.py or use environment variables:

MYSQL_user = "root"
MYSQL_pass = "your_password"
MYSQL_host = "localhost"
MYSQL_port = "3306"
MYSQL_database = "dairy"
▶️ Run the Project
uvicorn main:app --reload

Open:

http://127.0.0.1:8000/docs
🔐 API Endpoints
🟢 Signup
POST /signup

Request:

{
  "username": "mahi",
  "password": "Mahi@123"
}
🔵 Login
POST /login

Response:

"JWT_TOKEN_HERE"
🟡 Get All Users
GET /retrive
🔴 Delete User
DELETE /remove

Request:

{
  "username": "mahi"
}
🔒 Security Features
Passwords are hashed using bcrypt
JWT token used for authentication
Plain text passwords are never stored
⚠️ Notes
Do NOT store secrets (DB password, JWT secret) directly in code for production.
Use .env file for environment variables.
This project is for learning purposes.
🚀 Future Improvements
JWT expiration & refresh tokens
Role-based authentication (admin/user)
Email verification
Password reset system
Docker deployment
👨‍💻 Author

Built by Mahendra as a backend learning project using FastAPI.
