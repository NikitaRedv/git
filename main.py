from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db import create_table, get_connection

app = FastAPI()

create_table()

class UserCreate(BaseModel):
    username: str
    email: str

@app.get('/users')
def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return [{'id':u[0],'username':u[1], 'email':u[2]} for u in users]

@app.get('/users/{user_id}')
def get_user(user_id:int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.felchone()
    conn.close()
    if user:
        return {'id':user[0], 'username':user[1], 'email':user[2]}
    return HTTPException(status_code=404, detail="Користувача не знайдено")

@app.post("/create_user")
def create_user(user:UserCreate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email) VALUE (?,?)", (user.username, user.email))
    conn.commit()
    conn.close()
    return {"message": "user created"}