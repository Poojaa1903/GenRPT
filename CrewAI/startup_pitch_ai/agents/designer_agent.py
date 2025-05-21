from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

class DesignerAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def design(self, research_summary: str) -> str:
        prompt = f"Based on this research, design a product with unique selling points (USPs) and key features:\n{research_summary}"
        response = self.llm.invoke([HumanMessage(content=prompt)])
        return response.content
