from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

class MarketingAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def marketing_plan(self, product_design: str) -> str:
        prompt = f"Create a detailed marketing strategy and plan for this product:\n{product_design}"
        response = self.llm.invoke([HumanMessage(content=prompt)])
        return response.content
