from agents.researcher_agent import ResearcherAgent
from agents.designer_agent import DesignerAgent
from agents.marketing_agent import MarketingAgent
from agents.pitch_agent import PitchAgent

def main():
    print("Welcome to Startup Pitch AI!")
    idea = input("Enter your startup idea: ")

    researcher = ResearcherAgent()
    print("\n[ResearcherAgent] Researching market...")
    research_result = researcher.research(idea)
    print(research_result)

    designer = DesignerAgent()
    print("\n[DesignerAgent] Designing product...")
    design_result = designer.design(research_result)
    print(design_result)

    marketer = MarketingAgent()
    print("\n[MarketingAgent] Creating marketing plan...")
    marketing_result = marketer.marketing_plan(design_result)
    print(marketing_result)

    pitcher = PitchAgent()
    print("\n[PitchAgent] Creating final pitch...")
    pitch = pitcher.create_pitch(research_result, design_result, marketing_result)
    print("\n=== Final Startup Pitch ===\n")
    print(pitch)

if __name__ == "__main__":
    main()
