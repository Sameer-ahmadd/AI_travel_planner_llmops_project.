import streamlit as st
from src.core.planner import TravelAgent
from src.config.config import config


# streamlit functions
st.set_page_config(page_title="AI Travel Planner")
st.title("AI Travel Itineary Planner")
st.write("Plan your day trip itineary by entering your city and interests")


with st.form("Planner_form"):
    city = st.text_input("Enter the city you want to visit")
    interests = st.text_input("Enter your interests")
    submit_button = st.form_submit_button("Generate Itineary")


if submit_button:
    if city and interests:
        travel_agent = TravelAgent()
        travel_agent.set_city(city)
        travel_agent.set_interest(interests)
        itineary = travel_agent.create_itineary()
        st.subheader("📄 Your Itineary")
        st.markdown(itineary)
    else:
        st.warning("Please fill City or Interest to move forward")
