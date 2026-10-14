import streamlit as st
import pandas as pd
from database import add_student, get_students, get_student
from services import calculate_grade, calculate_statistics

# Səhifənin başlığı və dizaynı
st.title("🎓 Student Performance Dashboard")
st.write("Streamlit və Verilənlər Bazası vasitəsilə tələbə nəticələrinin idarə edilməsi.")

# --- BÖLÜM 1: Yeni Student Əlavə Etmək ---
st.header("Yeni Tələbə Əlavə Et")
with st.form("student_form"):
    student_name = st.text_input("Student Name")
    student_score = st.number_input("Score", min_value=0, max_value=100, step=1)
    submit_button = st.form_submit_button("Add Student")
    
    if submit_button:
        if student_name.strip() != "":
            add_student(student_name, student_score)
            st.success("Tələbə uğurla əlavə edildi!")
        else:
            st.warning("Zəhmət olmasa tələbənin adını daxil edin.")

# Bütün tələbələri bazadan çəkirik
raw_students = get_students()

# --- BÖLÜM 4: Statistikalar (Metrics) ---
st.header("📊 Statistikalar")
if raw_students:
    class StudentObj:
        def __init__(self, name, score):
            self.Name = name
            self.Score = score
            
    students_objs = [StudentObj(s[0], s[1]) for s in raw_students]
    stats = calculate_statistics(students_objs)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Students", stats["total_students"])
    col2.metric("Average Score", stats["average_score"])
    col3.metric("Highest Score", stats["highest_score"])
    col4.metric("Lowest Score", stats["lowest_score"])
else:
    st.info("Hələ ki bazada heç bir tələbə yoxdur.")

# --- BÖLÜM 2: Student Siyahısı və Grade Hesablanması ---
st.header("📋 Tələbələrin Siyahısı")
if raw_students:
    data = []
    for name, score in raw_students:
        grade = calculate_grade(score)
        data.append({"Name": name, "Score": score, "Grade": grade})
    
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
else:
    st.write("Göstəriləcək tələbə tapılmadı.")

# --- BÖLÜM 3: Student Axtarışı ---
st.header("🔍 Tələbə Axtarışı")
search_query = st.text_input("Search Student (Adına görə)")

if search_query:
    search_results = get_student(search_query)
    if search_results:
        search_data = []
        for name, score in search_results:
            grade = calculate_grade(score)
            search_data.append({"Name": name, "Score": score, "Grade": grade})
        
        search_df = pd.DataFrame(search_data)
        st.dataframe(search_df, use_container_width=True)
    else:
        st.warning(f"'{search_query}' adında tələbə tapılmadı.")