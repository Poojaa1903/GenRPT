import streamlit as st
from agents.researcher_agent import ResearcherAgent
from agents.dietician_agent import DieticianAgent
from agents.coach_agent import CoachAgent

st.set_page_config(page_title="AI Personal Fitness Coach", page_icon="💪", layout="centered")

st.title("🏋️ AI Personal Fitness Coach")
st.markdown("Let AI create your personalized fitness, diet and research-backed plans 💡")

with st.sidebar:
    st.header("🧍 Your Details")
    age = st.number_input("Age", min_value=10, max_value=100, value=25)
    weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
    goal = st.text_input("Fitness Goal", value="build muscle and lose fat")
    diet = st.selectbox("Diet Preference", ["vegetarian", "non-vegetarian", "both"])

    st.header("⚙️ Accessibility & Budget")
    no_gym = st.checkbox("No Gym Access?")
    low_budget = st.checkbox("Low Budget?")
    egg_only = st.checkbox("In Non-Veg, only Eggs?")

    generate = st.button("🚀 Generate Plan")

if generate:
    with st.spinner("Crunching your fitness data... 🧠💥"):
        # 🧾 User info dictionary with all fields
        user_info = {
            "age": age,
            "weight": weight,
            "goal": goal,
            "diet": diet,
            "no_gym": no_gym,
            "low_budget": low_budget,
            "egg_only": egg_only
        }

        # 👥 Agents
        researcher = ResearcherAgent()
        dietician = DieticianAgent()
        coach = CoachAgent()

        # 🔍 Generate outputs
        research_output = researcher.research(user_info)
        diet_output = dietician.create_diet_plan(user_info)
        workout_output = coach.create_workout_plan(user_info)

    # ✅ Display results
    st.success("Done! Here's your personalized plan 👇")

    st.subheader("🧠 Research Insights")
    st.write(research_output)

    st.subheader("🥗 Diet Plan")
    st.write(diet_output)

    st.subheader("🏋️ Workout Plan")
    st.write(workout_output)

else:
    st.info("Fill your details from the sidebar and click **Generate Plan** to begin.")
