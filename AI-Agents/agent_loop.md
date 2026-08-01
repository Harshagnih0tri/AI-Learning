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


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow
            if rev > (2**31 - 1) // 10 or (rev == (2**31 - 1) // 10 and digit > 7):
                return 0

            rev = rev * 10 + digit

        return sign * rev

| Commit                                      | Content Added                                           |
| ------------------------------------------- | ------------------------------------------------------- |
| `docs: initialize AI learning roadmap`      | Created AI Learning folder with roadmap and topics      |
| `docs: add AI fundamentals notes`           | AI, ML, DL, Generative AI basics                        |
| `docs: add LLM architecture notes`          | Transformers, attention, tokens, embeddings             |
| `docs: document prompt engineering basics`  | Prompting techniques and examples                       |
| `docs: add RAG learning notes`              | Retrieval-Augmented Generation explanation and workflow |
| `docs: add vector database concepts`        | Embeddings, similarity search, FAISS, Pinecone          |
| `docs: document LangChain fundamentals`     | Chains, prompts, memory, tools                          |
| `docs: add LangGraph workflow notes`        | Nodes, edges, state, agent flow                         |
| `docs: explain MCP architecture`            | Model Context Protocol overview                         |
| `docs: add AI agents overview`              | Agent loop, planning, reasoning, tools                  |
| `docs: compare AI automation frameworks`    | LangChain vs LangGraph vs CrewAI vs AutoGen             |
| `feat: add OpenAI API examples`             | Basic Python scripts using OpenAI API                   |
| `feat: add Ollama local model examples`     | Running local LLMs with Ollama                          |
| `feat: add Hugging Face inference examples` | Loading and using transformers                          |
| `feat: implement simple chatbot`            | Basic chatbot with conversation history                 |
| `feat: add embedding generation example`    | Generate and compare embeddings                         |
| `feat: build basic RAG prototype`           | PDF loader + vector DB + retrieval                      |
| `feat: create agent with tool calling`      | Calculator/search tool integration                      |
| `feat: add FastAPI AI endpoint`             | REST API serving an LLM                                 |
| `feat: add Streamlit chatbot UI`            | Simple frontend for chatbot                             |
| `test: add prompt evaluation examples`      | Prompt comparison experiments                           |
| `refactor: reorganize AI notes by topic`    | Better folder structure                                 |
| `docs: add interview preparation notes`     | AI interview Q&A                                        |
| `docs: summarize weekly AI learning`        | Progress log and takeaways                              |
| `chore: update learning resources`          | Added books, blogs, videos, papers                      |
AI-Learning/
│
├── 01_AI_Fundamentals/
├── 02_Prompt_Engineering/
├── 03_LLMs/
├── 04_RAG/
├── 05_Embeddings/
├── 06_Vector_Databases/
├── 07_LangChain/
├── 08_LangGraph/
├── 09_MCP/
├── 10_AI_Agents/
├── 11_Local_LLMs/
├── 12_API_Examples/
├── 13_Projects/
├── 14_Interview_Notes/
└── README.md








# AI vs ML

Artificial Intelligence (AI) is the broad field of creating systems that can perform tasks requiring human intelligence.

Machine Learning (ML) is a subset of AI where models learn patterns from data instead of being explicitly programmed.

Example:
- AI: ChatGPT, self-driving cars
- ML: Spam detection, recommendation systems

# Large Language Models

LLMs are neural networks trained on massive text datasets.

Key concepts:
- Tokens
- Context Window
- Parameters
- Temperature
- Top-p Sampling

# Prompt Engineering

Types:
- Zero-shot
- One-shot
- Few-shot
- Chain of Thought

A good prompt should be:
- Clear
- Specific
- Provide context
- Mention output format


# strings.py
text = "Hello World"

print(text.lower())
print(text.upper())
print(text.replace("World", "Python"))
print(text.split())
print(text[::-1])