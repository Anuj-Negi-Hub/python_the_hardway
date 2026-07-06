from fastapi import FastAPI

app = FastAPI() 

@app.get("/user")
def get_user():
    return {
        "id": 1,
        "name": "Anuj",
        "city": "Delhi"
    }
    #length of the name

@app.get("/get_length/{name}")
def get_length(name:str):
    given_name = name
    return {"length": len(given_name)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)