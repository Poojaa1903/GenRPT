from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage

# Setup environment variables and messages
load_dotenv()

messages = [
    SystemMessage("You are an expert in social media content strategy"), # Defines AI role
    HumanMessage("Give a short tip to craete engaging posts on Instagram") # Asks Questions
]

# ---- LangChain OpenAI Chat Model Example ----

# Create a ChatOpenAI model
llm = ChatOpenAI(model = "gpt-4o")

# Invoke the model with messages
result = llm.invoke(messages)
print(result.content)

# ---- Anthropic Chat Model Example ----

# Create a Anthropic model
model = ChatAnthropic(model="claude-3-opus-20240229")

result = model.invoke(messages)
print(f"Answer from Anthropic: {result.content}")

# ---- Google Chat Model Example ----

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

result = model.invoke(messages)
print(f"Answer from Google: {result.content}")