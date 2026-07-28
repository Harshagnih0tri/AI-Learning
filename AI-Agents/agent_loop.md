from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Explain {topic} in simple words."
)

print(prompt.format(topic="RAG"))

class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hi, I'm {self.name}"

s = Student("Harsh")
print(s.introduce())

steps = [
    "Load Documents",
    "Split Text",
    "Create Embeddings",
    "Store in Vector DB",
    "Retrieve Context",
    "Generate Answer"
]

for step in steps:
    print(step)

# AI Learning Repository

This repository contains my notes, code examples, mini-projects, and interview preparation while learning:

- Python
- FastAPI
- LLMs
- Prompt Engineering
- LangChain
- LangGraph
- RAG
- MCP
- AI Agents
- Google Gemini API

## Goals

- Build production-ready AI applications
- Learn Agentic AI
- Master backend development
- Prepare for AI/ML interviews
- Document daily learning