from dotenv import load_dotenv

load_dotenv()
"""

from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
response = model.invoke("Give me PAragraph on machine learning")
print(response.content)
from langchain.chat_models import init_chat_model
model = init_chat_model("groq:meta-llama/llama-4-scout-17b-16e-instruct")
response = model.invoke("what is meant by AI")
print(response.content)

"""
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
model = init_chat_model("mistral-small-2506")
print("----------------Welcome To ChatBot--------------")
print("Enter 0 for exit")
print("choose 1 for the angry mood")
print("choose 2 for the funny mood")
print("choose 3 for the sad mood")

choice=int(input("tell your response"))
if choice == 1:
    mood = "your act like a angry chat bot and reply everything in angry mood"
elif choice == 2:
    mood = "you act like a funny chat bot and reply everything in a funny way"
elif choice == 3:
    mood = "you act like a sad caht bot and reply everything in sad way"




messages=[
    SystemMessage(content=mood)
]
while True:
    prompt=input("you:")
    messages.append(HumanMessage(content=prompt))
    if prompt=="0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print(response.content)
