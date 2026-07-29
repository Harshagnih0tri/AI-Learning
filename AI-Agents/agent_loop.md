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

fastapi
uvicorn
langchain
langgraph
chromadb
faiss-cpu
sentence-transformers
openai
google-genai
python-dotenv
pydantic


# Learning Log

## Day 1
- Python revision
- OOP
- Git

## Day 2
- FastAPI Basics
- REST APIs

## Day 3
- Prompt Engineering

## Day 4
- LangChain

## Day 5
- RAG Pipeline

## Day 6
- AI Agents

## Day 7
- MCP

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

AI-Learning/
│── README.md
│── ROADMAP.md
│── LEARNING_LOG.md
│── RESOURCES.md
│── .gitignore
│── requirements.txt
│
├── AI-Agents/
│   ├── agent_loop.py
│   ├── tool_calling.py
│   ├── planner_executor.py
│   ├── memory.py
│   ├── notes.md
│   └── interview.md
│
├── Claude-Code/
│   ├── cli_commands.md
│   ├── best_practices.md
│   ├── prompts.md
│   └── notes.md
│
├── FastAPI/
│   ├── main.py
│   ├── crud.py
│   ├── auth.py
│   ├── middleware.py
│   ├── dependency_injection.py
│   ├── file_upload.py
│   └── notes.md
│
├── Google-AI/
│   ├── gemini_chat.py
│   ├── vision.py
│   ├── embeddings.py
│   └── notes.md
│
├── Interview/
│   ├── python.md
│   ├── fastapi.md
│   ├── rag.md
│   ├── llm.md
│   ├── langchain.md
│   ├── system_design.md
│   └── hr.md
│
├── LangChain/
│   ├── prompts.py
│   ├── output_parser.py
│   ├── memory.py
│   ├── chains.py
│   ├── retriever.py
│   ├── tools.py
│   └── notes.md
│
├── LangGraph/
│   ├── graph.py
│   ├── state.py
│   ├── conditional_edges.py
│   ├── checkpoint.py
│   └── notes.md
│
├── LLM/
│   ├── tokenizer.py
│   ├── attention.md
│   ├── transformers.md
│   ├── inference.md
│   ├── quantization.md
│   └── fine_tuning.md
│
├── MCP/
│   ├── client.py
│   ├── server.py
│   ├── tools.md
│   └── notes.md
│
├── Projects/
│   ├── chatbot/
│   ├── ai-agent/
│   ├── rag-chatbot/
│   ├── pdf-chat/
│   └── resume-analyzer/
│
├── Prompt-Engineering/
│   ├── zero_shot.md
│   ├── one_shot.md
│   ├── few_shot.md
│   ├── cot.md
│   ├── react.md
│   ├── system_prompts.md
│   └── examples.md
│
├── Python/
│   ├── basics.py
│   ├── oop.py
│   ├── decorators.py
│   ├── generators.py
│   ├── context_manager.py
│   ├── multithreading.py
│   ├── async.py
│   └── interview.md
│
├── RAG/
│   ├── embeddings.py
│   ├── chunking.py
│   ├── vector_db.py
│   ├── faiss.py
│   ├── chromadb.py
│   ├── pipeline.py
│   └── notes.md
│
└── Resources/
    ├── books.md
    ├── courses.md
    ├── roadmap.md
    ├── glossary.md
    └── cheatsheet.md   
    Content

Added notes on:
Agentic AI
AI Automation
MCP (Model Context Protocol)
API vs MCP
AI Skills
Agent workflow

GET
POST
PUT
PATCH
DELETE
Status codes
Request/Response cycle

# inheritance
# polymorphism
# abstraction
# encapsulation

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()

git commit -m "feat: add Python OOP revision examples"

Include:

Mutable vs Immutable
List vs Tuple
Decorators
Generators
*args **kwargs
GIL
OOP concepts