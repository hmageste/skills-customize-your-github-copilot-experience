from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Assignment(BaseModel):
    title: str
    description: str
    completed: bool = False


sample_assignments = [
    {"id": 1, "title": "Read Chapter 1", "description": "Review the API basics chapter.", "completed": False},
    {"id": 2, "title": "Write Endpoints", "description": "Create your first FastAPI routes.", "completed": True},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the assignment API"}


@app.get("/assignments")
def get_assignments():
    return sample_assignments


@app.get("/assignments/{assignment_id}")
def get_assignment(assignment_id: int):
    for assignment in sample_assignments:
        if assignment["id"] == assignment_id:
            return assignment
    return {"error": "Assignment not found"}


@app.post("/assignments")
def create_assignment(assignment: Assignment):
    return {
        "message": "Assignment created successfully",
        "assignment": assignment,
    }