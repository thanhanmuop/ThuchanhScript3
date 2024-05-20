from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Student(BaseModel):
    id: int
    name: str
    age: int
    address: str
    phone: str
    email: str
    class_name: str

class LoginRequest(BaseModel):
    username: str
    password: str

students = [
    Student(id=1, name="Hà Huy Hoàng", age=20, address="Hà Nội", phone="0123456789", email="hoang@gmail.com", class_name="UDU-01"),
    Student(id=2, name="Bùi Thị Yến", age=21, address="Hải Phòng", phone="0987654321", email="yen@gmail.com", class_name="UDU-02"),
    Student(id=2, name="Trần Văn Ngà", age=19, address="Thái Bình", phone="0982563421", email="nga@gmail.com", class_name="UDU-03"),
    Student(id=2, name="Phạm Khánh Linh", age=20, address="Hưng Yên", phone="0258456325", email="linh@gmail.com", class_name="UDU-04"),
    # Thêm các sinh viên khác
]

@app.post("/login")
def login(request: LoginRequest):
    if request.username == "admin" and request.password == "admin":
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Tài khoản hoặc mật khẩu không chính xác")

@app.get("/students", response_model=List[Student])
def get_students():
    return students

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
