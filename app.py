import streamlit as st 
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="DataVision",
    page_icon="📊",
    layout="wide"
    )

# Load data
df = pd.read_csv("student_old.csv")
df.column = df.columns.str.strip()
print(df.columns.tolist())

#Title
st.title("📊 DataVision")
st.subheader("Student Performance Analytics Dashboard")

st.divider()

#Dashboard metrics
col1,  col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📚 Subjects" ,4)

with col2:
    st.metric("📈 Average Marks",round(df["Average"].mean (),2))

with col3:
    st.metric("📅 Avg Attendance","N/A")
    st.divider()

# Dataset[]
st.subheader("📋 Student Dataset")

st.dataframe(
    df,
    use_container_width = True
)
st.subheader("📊 Average Marks by Subjects")

subjects = ["Math","Science","English","Physics"]
average_marks = df[subjects].mean()

st.bar_chart(average_marks)
st.subheader("🎓 Student-wise performance")

student_marks = df.set_index("Nmae")
[["Math","Science","English","Physics"]]
print(df.columns)
print(df.dtypes)
