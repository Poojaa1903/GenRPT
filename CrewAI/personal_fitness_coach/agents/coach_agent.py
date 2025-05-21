import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()

class CoachAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4", temperature=0.7)

    def create_workout_plan(self, user_info):
        prompt = (
            f"Create a 4-week workout plan for someone who is {user_info['age']} years old, "
            f"{user_info['weight']} kg, and wants to {user_info['goal']}."
        )
        response = self.llm.invoke([HumanMessage(content=prompt)])
        return response.content
        
        if user_info.get("no_gym"):
            prompt += "\nNote: The user doesn't have access to a gym. Suggest only home-based exercises using bodyweight or minimal equipment (like resistance bands)."
