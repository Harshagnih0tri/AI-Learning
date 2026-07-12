import json

student = {
    "name": "Harsh Sharma",
    "goal": "AI Engineer",
    "skills": [
        "Python",
        "Git",
        "FastAPI",
        "Machine Learning"
    ]
}

print(json.dumps(student, indent=4))