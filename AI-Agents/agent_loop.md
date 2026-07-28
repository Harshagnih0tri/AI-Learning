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