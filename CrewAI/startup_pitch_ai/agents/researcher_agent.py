from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

class ResearcherAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def research(self, startup_idea: str) -> str:
        prompt = f"Do detailed market research on this startup idea: {startup_idea}. Tell me about competitors, target customers, and market trends."
        response = self.llm.invoke([HumanMessage(content=prompt)])
        return response.content
