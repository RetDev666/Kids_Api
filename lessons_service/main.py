from fastapi import FastApi, FastAPI

app = FastAPI(title="Lessons Service")
LESSONS = [
    {"id": 1, "title": "Що таке API?"},
    {"id": 2, "title": "Методи HTTP"},
    {"id": 3, "title": "Json і статус-коди"},
]
@app.get("/lessons")
def get_lessons():
    return LESSONS