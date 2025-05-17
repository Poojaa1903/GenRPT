from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Setup environment variables
load_dotenv()

# Create a ChatOpenAI model
llm = ChatOpenAI(model = "gpt-4o")

# Invoke the model with messages
result = llm.invoke("What is the square root of 400")
print(result.content)