from agents.researcher_agent import ResearcherAgent
from agents.dietician_agent import DieticianAgent
from agents.coach_agent import CoachAgent

def main():
    print("Welcome to AI Personal Fitness Coach!\n")

    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight (kg): "))
    goal = input("Enter your fitness goal (e.g. build muscle, lose fat): ")
    diet = input("Enter your diet preference (e.g. vegetarian, non-vegetarian): ")
    no_gym = input("No gym access? (yes/no): ").lower() == "yes"
    low_budget = input("Low budget? (yes/no): ").lower() == "yes"
    egg_only = input("In non-veg, only eggs? (yes/no): ").lower() == "yes"

    user_info = {
        "age": age,
        "weight": weight,
        "goal": goal,
        "diet": diet,
        "no_gym": no_gym,
        "low_budget": low_budget,
        "egg_only": egg_only
    }

    researcher = ResearcherAgent()
    dietician = DieticianAgent()
    coach = CoachAgent()

    market_insights = researcher.research(user_info)
    diet_plan = dietician.create_diet_plan(user_info)
    workout_plan = coach.create_workout_plan(user_info)

    print("\n===== Personalized Plan =====\n")
    print("[🧠 Research Insights]\n", market_insights)
    print("\n[🥗 Diet Plan]\n", diet_plan)
    print("\n[🏋️ Workout Plan]\n", workout_plan)

if __name__ == "__main__":
    main()
