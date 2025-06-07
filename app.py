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

bookings = []

# Sidebar user role
user_type = st.sidebar.radio("I am a...", ["Player", "Coach"])

# Main App Title
st.title("🎾 TennisBuddy")

# Tabs
tabs = st.tabs(["🏠 Home", "🎯 Find Partner", "📅 Book Coach", "📍 Map"])

# --- HOME TAB ---
with tabs[0]:
    st.header("📝 Create Your Profile")
    name = st.text_input("Name", key="name_home")
    age = st.slider("Age", 10, 70, key="age_home")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="gender_home")
    level = st.selectbox("Skill Level", ["Beginner", "Intermediate", "Advanced", "Pro"], key="level_home")

    if user_type == "Coach":
        st.subheader("📢 Coach Profile Setup")
        rate = st.text_input("Hourly Rate (e.g., $50/hr)", key="rate_home")
        specialties = st.text_area("Specialties", key="specialties_home")
        availability = st.text_input("Availability", key="availability_home")
        if st.button("Save My Profile"):
            new_coach = {"name": name, "rate": rate, "specialties": specialties, "availability": availability}
            coaches.append(new_coach)
            st.success("✅ Coach profile saved!")

        st.write("### 📖 My Bookings")
        my_bookings = [b for b in bookings if b['coach'] == name]
        if my_bookings:
            for b in my_bookings:
                st.write(f"📅 {b['time']} | Player: {b['player']}")
        else:
            st.info("No bookings yet.")

# --- FIND PARTNER TAB ---
with tabs[1]:
    if user_type == "Player":
        st.header("🎯 Find a Hitting Partner")
        preferred_gender = st.selectbox("Preferred Gender", ["Any", "Male", "Female"])
        preferred_level = st.selectbox("Preferred Level", ["Any", "Beginner", "Intermediate", "Advanced"])
        availability = st.text_input("Availability (e.g., evenings, weekends)", key="availability_partner")

        if st.button("🔍 Match Me"):
            st.success("Matching partners...")
            filtered = [p for p in players if 
                        (preferred_gender == "Any" or p['gender'] == preferred_gender) and
                        (preferred_level == "Any" or p['level'] == preferred_level)]
            st.write("### 🎾 Potential Partners")
            for p in filtered:
                st.write(f"**{p['name']}** | {p['age']} y/o | {p['level']} | Available: {p['availability']}")
    else:
        st.info("Only players can search for hitting partners.")

# --- BOOK COACH TAB ---
with tabs[2]:
    if user_type == "Player":
        st.header("📅 Book a Coach")
        for coach in coaches:
            st.write(f"**{coach['name']}** | {coach['rate']} | Specialties: {coach['specialties']} | Available: {coach['availability']}")
            if st.button(f"📅 Book {coach['name']}", key=f"book_{coach['name']}"):
                bookings.append({
                    "coach": coach['name'],
                    "player": name,
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M")
                })
                st.success(f"Booking request sent to {coach['name']}!")
    else:
        st.info("Only players can book coaches.")

# --- MAP TAB ---
with tabs[3]:
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


st_folium(court_map, width=700, height=450)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Youssef")
