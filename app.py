import streamlit as st
from ml import predict_performance
st.set_page_config(page_title="Student Performance Predictor")
st.title("🎓 Student Performance Prediction")
st.write("Enter student details to predict performance index")
# Input fields
hours = st.number_input("Hours Studied per day", 0.0, 24.0, step=1.0)
prev = st.number_input("Previous Scores", 0.0, 100.0)
extra = st.selectbox("Extracurricular Activities", ["No", "Yes"])
sleep = st.number_input("Sleep Hours per day", 0.0, 12.0)
sample = st.number_input("Sample Question Papers Practiced", 0, 50)
extra = 1 if extra == "Yes" else 0
if st.button("Predict Performance"):
    result = predict_performance(hours, prev, extra, sleep, sample)
    st.success(f"Predicted Performance Index: {result:.2f}")
    if result > 80:
        st.success("Excellent performance expected 🎉")
    elif result > 60:
        st.info("Good performance 👍")
    else:
        st.warning("Needs improvement ⚠️")
st.sidebar.title("🎓 Student Performance Prediction App")
st.sidebar.subheader("📘 About App")
st.sidebar.write(
    "This ML-based app predicts student performance "
    "using study habits and lifestyle inputs."
)
st.sidebar.subheader("⚙️ How It Works")
st.sidebar.write("""
• Data preprocessing  
• Feature scaling  
• Linear Regression  
• Real-time prediction  
""")
st.sidebar.subheader("📊 Model Performance")
st.sidebar.info("R² Score ≈ 0.98")
st.sidebar.info("Low Mean Squared Error ")
st.sidebar.subheader("🛠 Tech Stack")
st.sidebar.write("""
• Python  
• Pandas 
• Scikit-learn  
• Streamlit  
""")
st.sidebar.subheader("👨‍💻 Developer")
st.sidebar.write("Irfan Khan")
st.sidebar.write("BTech CSE | Central University of Punjab")
st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #e0f2fe;
}
/* Predict button */
div.stButton > button {
    background-color: pink;
    color: white;
    border-radius: 25px;
    height: 3em;
}
/* Result box */
.stAlert {
    border-radius: 15px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

