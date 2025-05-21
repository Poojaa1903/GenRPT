import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()

class DieticianAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4", temperature=0.7)

    def create_diet_plan(self, user_info):
        prompt = (
            f"Create a weekly diet plan for a {user_info['age']} year old who is {user_info['diet']} "
            f"and wants to {user_info['goal']}. Current weight is {user_info['weight']} kg."
        )
        response = self.llm.invoke([HumanMessage(content=prompt)])
        return response.content
        
        if user_info.get("low_budget"):
            prompt += "\nNote: The user has a low budget, so use affordable food options like lentils, rice, oats, bananas, etc."

        if user_info.get("egg_only"):
            prompt += "\nNote: The user is non-vegetarian but only consumes eggs. Exclude all other meats and focus on high-protein vegetarian options and eggs."

