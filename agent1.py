# from typing_extensions import TypedDict
# from typing import Annotated
# from langchain_core.messages import AnyMessage
# from langgraph.graph.message import add_messages
# from langchain_community.chat_models import ChatOllama

# class State(TypedDict):
#     messages: Annotated[list[AnyMessage], add_messages]
#     completed: bool
    
# from dotenv import load_dotenv
# import os
# # load_dotenv()
# # os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API")
# # llm = ChatGroq(model="llama-3.1-8b-instant")
# llm = ChatOllama(model="phi3", temperature=0.7)

# prompt = """You are an AI chatbot assigned to help the user decide their career path.
# - Ask questions related to CS fields
# - Ask only one question at a time
# - Maximum 5 questions

# - STRICT RULES:
# - Ask ONLY ONE question at a time
# - Do NOT ask multiple questions together
# - Do NOT give final answer early
# - Wait for user reply

# If you break rules, your answer is invalid.
# - End with giving a single carrer option with reasoning, starting with the phrase:
# FINAL ANSWER:
# """

# def chat_step(messages):
#     if len(messages) == 0:
#         messages.append({"role": "system", "content": prompt})

#     response = llm.invoke(messages)
#     content = response.content.split("\n")[0]
#     messages.append({
#         "role": "assistant",
#         "content": response.content
#     })
#     completed = "FINAL ANSWER:" in response.content
#     return messages, response.content, completed


from typing_extensions import TypedDict
from typing import Annotated
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages
from langchain_community.chat_models import ChatOllama

class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    completed: bool
    step: int

llm = ChatOllama(
    model="phi3",   
    temperature=0.7
)

questions = [
    "What aspects of computer science interest you most?",
    "Do you have experience with Python or Java?",
    "Do you prefer theory, algorithms, or practical development?",
    "Any specific industries you like (finance, healthcare, etc.)?",
    "How important is continuous learning for you?"
]

final_prompt = """Based on the user's answers, suggest ONE suitable CS career path.

Give:
- Career name
- Clear reasoning
Start with:
FINAL ANSWER:
"""

def chat_step(messages, step):
    if len(messages) == 0:
        messages.append({"role": "system", "content": final_prompt})
    if step < len(questions):
        question = questions[step]

        messages.append({
            "role": "assistant",
            "content": question
        })
        return messages, question, False, step + 1
    else:
        response = llm.invoke(messages)
        content = response.content
        if not content.startswith("FINAL ANSWER:"):
            content = "FINAL ANSWER:\n" + content

        messages.append({
            "role": "assistant",
            "content": content
        })
        return messages, content, True, step