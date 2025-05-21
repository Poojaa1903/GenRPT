from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

class PitchAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def create_pitch(self, research: str, design: str, marketing: str) -> str:
        prompt = f"""
        Create a compelling startup pitch based on:
        Research: {research}
        Design: {design}
        Marketing: {marketing}
        Make it investor-friendly and convincing.
        """
        response = self.llm.invoke([HumanMessage(content=prompt)])
        return response.content
