# src/main.py

import sys
import os
sys.path.append(os.path.dirname(__file__))  # добавляем папку src в путь поиска модулей

import streamlit as st
from mock_data import default_data
from logic import check_rules

st.title("HR Rule-Based System 🛠")

st.write("### Настройка данных кандидата")

position = st.sidebar.text_input("Должность:", value=default_data["position_applied"])
experience = st.sidebar.number_input("Опыт (месяцы):", value=default_data["experience_months"])
has_contacts = st.sidebar.checkbox("Есть контакты:", value=default_data["has_contacts"])

all_skills = ["Python", "SQL", "Git", "Java", "C++", "Cobol", "VB6"]
selected_skills = st.sidebar.multiselect("Навыки кандидата:", options=all_skills, default=default_data["skills"])

if st.button("Запустить проверку"):
    candidate_data = {
        "position_applied": position,
        "experience_months": experience,
        "has_contacts": has_contacts,
        "skills": selected_skills
    }
    result = check_rules(candidate_data)
    
    if "✅" in result:
        st.success(result)
    elif "⛔️" in result:
        st.error(result)
    else:
        st.warning(result)
