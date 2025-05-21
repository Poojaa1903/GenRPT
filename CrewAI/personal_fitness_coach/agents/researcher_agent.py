import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()

class ResearcherAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4", temperature=0.7)

    def research(self, user_info):
        prompt = f"Research recent fitness trends for a {user_info['age']} year old aiming to {user_info['goal']}."
        response = self.llm.invoke([HumanMessage(content=prompt)])
        return response.content
