from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class OperationInput(BaseModel):
    a: float
    b: float

@app.post("/add")
def add(input: OperationInput):
    return {"result": input.a + input.b}

@app.post("/subtract")
def subtract(input: OperationInput):
    return {"result": input.a - input.b}

@app.post("/multiply")
def multiply(input: OperationInput):
    return {"result": input.a * input.b}

@app.post("/divide")
def divide(input: OperationInput):
    if input.b == 0:
        return {"error": "Không thể chia cho 0"}
    return {"result": input.a / input.b}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
