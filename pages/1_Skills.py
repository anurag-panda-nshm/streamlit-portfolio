import streamlit as st
import json
import os

st.title("🛠 Skills & Technologies")

def load_skills():
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to the parent directory
    parent_dir = os.path.dirname(current_dir)
    # Construct path to skills.json
    json_path = os.path.join(parent_dir, "skills.json")
    try:
        with open(json_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("skills.json file not found!")
        return []

# Load skills from JSON
skills = load_skills()

# Group skills into categories (3 columns)
total_skills = len(skills)
skills_per_col = total_skills // 3 + (1 if total_skills % 3 != 0 else 0)

# Display in grid format
cols = st.columns(3)
for index, skill in enumerate(skills):
    with cols[index // skills_per_col]:
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image(skill["icon"], width=40)
        with col2:
            st.markdown(f"**{skill['name']}**")

