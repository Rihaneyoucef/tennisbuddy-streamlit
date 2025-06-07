# app.py
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import datetime

# Mock database (in memory for now)
players = [
    {"name": "Sarah", "age": 16, "gender": "Female", "level": "Intermediate", "availability": "Weekends"},
    {"name": "Omar", "age": 25, "gender": "Male", "level": "Advanced", "availability": "Evenings"},
    {"name": "Lina", "age": 30, "gender": "Female", "level": "Beginner", "availability": "Mornings"},
]

coaches = [
    {"name": "Coach Mike", "rate": "$50/hr", "specialties": "Serve, Movement", "availability": "Weekdays 5-8PM"},
    {"name": "Coach Amina", "rate": "$40/hr", "specialties": "Beginners, Kids", "availability": "Weekends Only"},
]

# Sidebar
user_type = st.sidebar.radio("I am a...", ["Player", "Coach"])

st.title("🎾 TennisBuddy")

# Profile creation
st.header("📝 Create Your Profile")
name = st.text_input("Name")
age = st.slider("Age", 10, 70)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
level = st.selectbox("Skill Level", ["Beginner", "Intermediate", "Advanced", "Pro"])

# Player side
if user_type == "Player":
    st.subheader("🎯 Find a Hitting Partner")
    preferred_gender = st.selectbox("Preferred Gender", ["Any", "Male", "Female"])
    preferred_level = st.selectbox("Preferred Level", ["Any", "Beginner", "Intermediate", "Advanced"])
    availability = st.text_input("Availability (e.g., evenings, weekends)")
    if st.button("🔍 Match Me"):        
        st.success("Matching partners...")
        filtered = [p for p in players if 
                    (preferred_gender == "Any" or p['gender'] == preferred_gender) and
                    (preferred_level == "Any" or p['level'] == preferred_level)]
        st.write("### 🎾 Potential Partners")
        for p in filtered:
            st.write(f"**{p['name']}** | {p['age']} y/o | {p['level']} | Available: {p['availability']}")

# Coach side
if user_type == "Coach":
    st.subheader("📅 Coach Dashboard")
    rate = st.text_input("Hourly Rate (e.g., $50/hr)")
    specialties = st.text_area("Specialties")
    availability = st.text_input("Availability")
    if st.button("📢 Save My Profile"):
        st.success("Coach profile saved!")
        st.write(f"**{name}** | Rate: {rate} | Available: {availability}")

# Show coaches
st.markdown("---")
st.header("🧑‍🏫 Available Coaches")
for coach in coaches:
    st.write(f"**{coach['name']}** | {coach['rate']} | Specialties: {coach['specialties']} | Available: {coach['availability']}")
    st.button(f"📅 Book {coach['name']}", key=coach['name'])

# Map of courts (mock locations)
st.markdown("---")
st.header("📍 Find Nearby Courts")
court_map = folium.Map(location=[25.276987, 55.296249], zoom_start=12)
courts = [
    {"name": "Central Park Court", "lat": 25.276987, "lon": 55.296249},
    {"name": "Lakeside Tennis", "lat": 25.290, "lon": 55.31},
    {"name": "Greenfield Club", "lat": 25.265, "lon": 55.28},
]
for court in courts:
    folium.Marker([court['lat'], court['lon']], tooltip=court['name']).add_to(court_map)

st_folium(court_map, width=700, height=450)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Youssef")
