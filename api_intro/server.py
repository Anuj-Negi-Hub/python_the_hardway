from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Basic FastAPI Server",
    description="A simple API server to demonstrate GET and POST requests.",
    version="1.0.0"
)

# Define a Pydantic model for our POST payload
class PayloadData(BaseModel):
    name: str
    description: Optional[str] = None
    value: float
    tax: Optional[float] = None

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the basic FastAPI server!",
        "status": "running"
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {
        "item_id": item_id,
        "query_param": q,
        "status": "success"
    }

@app.post("/submit")
def create_item(payload: PayloadData):
    # Calculate some result using the payload
    total_value = payload.value
    if payload.tax:
        total_value += payload.value * payload.tax
        
    return {
        "received_payload": payload.model_dump() if hasattr(payload, 'model_dump') else payload.dict(),
        "calculated_total": total_value,
        "message": f"Hello {payload.name}, your payload was processed successfully."
    }

if __name__ == "__main__":
    import uvicorn
    # Run server locally on port 8000
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
