from flask import (
    Flask,
    request
)
from app.database import task

app = Flask(__name__)

# REST - Representational State Transfer - Architectural design pattern for
# building network connected services. 


@app.get("/")
@app.get("/tasks")
def scan():
    out = {
        "tasks": task.scan(),
        "ok": True
    }
    return out                  # by default, Flask will return a status code of 200

@app.put("/tasks/<int:pk>/")
def update(pk):
    task_data = request.json
    task.update_by_id(task_data, pk)
    return "", 204               # 204 is no content (successful, but there's nothing to return)

@app.post("/tasks")
def create():
    task_data = request.json
    task.insert(task_data)
    return "", 204

@app.delete("/tasks/<int:pk>/")
def delete(pk):
    task.delete_by_id(pk)
    return "", 204

@app.get("/tasks/<int:pk>/")
def select_by_id(pk):
    out = {
        "tasks": task.select_by_id(),
        "ok": True
    }
    return out