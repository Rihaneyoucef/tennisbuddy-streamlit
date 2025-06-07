import streamlit as st

# Sidebar login simulation
user_type = st.sidebar.radio("I am a...", ["Player", "Coach"])

st.title("🎾 TennisBuddy")

# Profile creation
st.header("📝 Create Your Profile")
name = st.text_input("Name")
age = st.slider("Age", 10, 70)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
level = st.selectbox("Skill Level", ["Beginner", "Intermediate", "Advanced", "Pro"])

if user_type == "Player":
    st.subheader("🎯 Looking for a Hitting Partner")
    preferred_gender = st.selectbox("Preferred Gender", ["Any", "Male", "Female"])
    preferred_level = st.selectbox("Preferred Level", ["Any", "Beginner", "Intermediate", "Advanced"])
    availability = st.text_input("Available Time Slots (e.g., evenings, weekends)")
    st.button("🔍 Find Partners")

elif user_type == "Coach":
    st.subheader("📅 Set Availability")
    rate = st.text_input("Hourly Rate (USD)")
    specialties = st.text_area("Specialties (e.g., serve, footwork, kids)")
    st.button("📢 Make Myself Available")

st.markdown("---")
st.header("📍 Find a Tennis Court (Coming Soon)")
st.info("We'll soon add a court map here using OpenStreetMap!")

