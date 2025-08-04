import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("college_student_management_data.csv")
st.title("College Student Management Dataset")
st.write(data)
st.write("Length of table:", len(data))

def plot_pie(pie_element, title):
    plt.figure(figsize=(4, 2))
    plt.pie(pie_element.values, labels=pie_element.index, autopct="%1.1f%%")
    plt.axis("equal")
    plt.title(title, fontsize=8)
    st.pyplot(plt)

def display_avg(item, group_item, target_item, title):
    avg_data = item.groupby(group_item)[target_item].mean().sort_values(ascending=False).reset_index()
    avg_data.columns = [group_item.capitalize(), f"Average {target_item}"]
    st.subheader(title)
    st.write(avg_data)

def display_count(item, group_item, title):
    count_data = item[group_item].value_counts()
    st.subheader(title)
    st.write(count_data)
    plot_pie(count_data, f"{title}")

def higher_than_avg(item, target_item, title):
    mean_value = item[target_item].mean()
    lower_than = item[mean_value < item[target_item]].sort_values(by=[target_item])
    st.subheader(title)
    st.write(lower_than)
    st.write(f"Average {target_item}: {mean_value:.2f}")
    st.write(f"Total count: {len(lower_than)}")

# Age
display_avg(data, "major", "age", "Average Age by major")

st.subheader("Count of students, who older than average age")
count_students_who_older_than_avg = data[data["age"] > data["age"].mean()].sort_values(by=["age"], ascending=False)
st.write(count_students_who_older_than_avg)
st.write(count_students_who_older_than_avg["gender"].value_counts())
st.write(f"Total: {len(count_students_who_older_than_avg)}")

# Gender
display_count(data, "gender", "Count of each gender")

# Major
display_count(data, "major", "Count of students in each major")

# GPA
display_avg(data, "major", "GPA", "Average GPA for each major.")
display_avg(data, "gender", "GPA", "Average GPA by gender.")

st.subheader("Average GPA by major for each gender(sorted)")
avg_gpa_by_major_each_gender = data.groupby(["major", "gender"])["GPA"].mean().sort_values(ascending=False)
st.write(avg_gpa_by_major_each_gender)

st.subheader("Count of students with GPA more than 3")
count_gender_with_gpa_more_3 = data[data["GPA"] > 3].groupby(["major", "gender"])["GPA"].count().sort_values(ascending=False)
st.write(count_gender_with_gpa_more_3)

higher_than_avg(data, "GPA", "Count of students, who have higher than average GPA")

# Course Grade
display_avg(data, "major", "avg_course_grade", "Average grade for courses for each specialty")
display_avg(data, "gender", "avg_course_grade", "Average grade for courses for each gender")

higher_than_avg(data, "avg_course_grade", "Count of students, who have higher than average grade")

# Attendance rate
display_avg(data, "major", "attendance_rate", "Average attendance level by specialty")
display_avg(data, "gender", "attendance_rate", "Average attendance level by gender")

st.subheader("Average attendance level by speciality for each gender(sorted)")
avg_attendance_by_major_each_gender = data.groupby(["major", "gender"])["attendance_rate"].mean().sort_values(ascending=False)
st.write(avg_attendance_by_major_each_gender)

# LMS and Session Duration
st.subheader("LMS")
avg_lms_login = data["lms_logins_past_month"].mean()
st.write("Average number of logins to LMS per month:", avg_lms_login)

st.subheader("Session Duration")
avg_session_duration = data["avg_session_duration_minutes"].mean()
st.write("Average session duration..", avg_session_duration)

# Forum and video
st.subheader("Forum and video participation rate (average)")

avg_forum_participation = data["forum_participation_count"].mean()
st.write("Forum Participation Level:", avg_forum_participation)

avg_video_completion = data["video_completion_rate"].mean()
st.write("Video participation rate:", avg_video_completion)

# Risk Level
display_count(data, "risk_level", "Count of risk level of students")

st.subheader("The best Students Statistics")
best_students = data[
    (data["GPA"] >= 3.5) &
    (data["avg_course_grade"] > data["avg_course_grade"].mean()) &
    (data["enrollment_status"] == "Active")
].sort_values(by=["GPA"], ascending=False)
st.write(best_students)
st.write(best_students["major"].value_counts())
st.write(f"Total: {len(best_students)} students")

st.subheader("The worst Students Statistics")
worst_students = data[
    (data["GPA"] >= 2.5) &
    (data["avg_course_grade"] < data["avg_course_grade"].mean()) &
    (data["enrollment_status"] == "Leave")
].sort_values(by=["GPA"], ascending=True)
st.write(worst_students)
st.write(worst_students["major"].value_counts())
st.write(f"Total: {len(worst_students)} students")