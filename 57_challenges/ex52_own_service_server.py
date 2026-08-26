from fastapi import FastAPI
from datetime import datetime


app = FastAPI()

@app.get("/time")
def get_time():
    current_time = datetime.now()

    return {
        "currentime": current_time.strftime("%Y-%M-%D %H:%M:%S")
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
