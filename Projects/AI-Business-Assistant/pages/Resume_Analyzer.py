import streamlit as st
from PyPDF2 import PdfReader
from utils import ask_ai
import re

# Page Configuration
st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Title
st.title("📄 AI Resume Analyzer")

# Score Cards
col1, col2 = st.columns(2)

with col1:
    st.metric("Resume Score: xx/100")

with col2:
    st.metric("ATS Score: xx /100")

# Progress Bars
st.progress(0)
st.caption("Resume Score")

st.progress(0)
st.caption("ATS Score")

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

# If file uploaded
if uploaded_file:

    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    st.success("✅ Resume Uploaded Successfully!")

    if st.button("Analyze Resume"):

        prompt = f"""
You are an expert HR Recruiter.

Analyze this resume and provide:

1. Resume Score (out of 100)
2. ATS Score
3. Strengths
4. Weaknesses
5. Missing Skills
6. Suggestions for Improvement

Resume:

{resume_text}
"""

        with st.spinner("🤖 Analyzing Resume..."):
            answer = ask_ai(prompt)

        st.subheader("📋 Resume Analysis")

        st.markdown(answer)
        resume_score = 0
ats_score = 0

resume_match = re.search(r"Resume Score.*?(\d+)", answer, re.IGNORECASE)
ats_match = re.search(r"ATS Score.*?(\d+)", answer, re.IGNORECASE)

if resume_match:
    resume_score = int(resume_match.group(1))

if ats_match:
    ats_score = int(ats_match.group(1))

st.subheader("📊 Scores")

col1, col2 = st.columns(2)

with col1:
    st.metric("Resume Score", f"{resume_score}/100")
    st.progress(resume_score)

with col2:
    st.metric("ATS Score", f"{ats_score}/100")
    st.progress(ats_score)

    st.download_button(
            label="📥 Download Analysis",
            data=answer,
            file_name="resume_analysis.txt",
            mime="text/plain"
        )