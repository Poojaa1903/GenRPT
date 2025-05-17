from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Setup environment variables and messages
load_dotenv()

messages = [
    SystemMessage("You are an expert in social media content strategy"), # Defines AI role
    HumanMessage("Give a short tip to craete engaging posts on Instagram") # Asks Questions
]

# Create a ChatOpenAI model
llm = ChatOpenAI(model = "gpt-4o")

# Invoke the model with messages
result = llm.invoke(messages)
print(result.content)