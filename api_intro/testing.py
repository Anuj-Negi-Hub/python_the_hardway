from fastapi import FastAPI

app = FastAPI()

students = {
    1: {
        "name": "Anuj",
        "age": 22,
        "city": "Bangalore"
    }
}

print(type(app))
print(type(students))