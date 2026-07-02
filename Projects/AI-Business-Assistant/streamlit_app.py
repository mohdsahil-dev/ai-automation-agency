import streamlit as st
from utils import ask_ai
from prompts import (
    EMAIL_PROMPT,
    LINKEDIN_PROMPT,
    RESUME_PROMPT
)

st.set_page_config(
    page_title="AI Business Assistant",
    page_icon="🤖",
    layout="wide"
)

st.sidebar.title("🤖 AI Business Assistant")

menu = st.sidebar.radio(
    "Choose Tool",
    [
        "AI Chat",
        "Email Generator",
        "Resume Improver",
        "LinkedIn Post"
    ]
)

st.title(menu)

if menu == "AI Chat":

    # Chat History
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Purane messages dikhana
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Naya message
    if prompt := st.chat_input("Ask me anything..."):

        # User Message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        # AI Response
        with st.chat_message("assistant"):

            with st.spinner("🤖 Thinking..."):

                answer = ask_ai(prompt)

                st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

elif menu == "Email Generator":

    topic = st.text_area("Email Topic")

    if st.button("Generate Email"):
        answer = ask_ai(EMAIL_PROMPT + topic)
        st.write(answer)

elif menu == "Resume Improver":

    resume = st.text_area("Paste Resume")

    if st.button("Improve Resume"):
        answer = ask_ai(RESUME_PROMPT + resume)
        st.write(answer)

elif menu == "LinkedIn Post":

    topic = st.text_area("Topic")

    if st.button("Generate Post"):
        answer = ask_ai(LINKEDIN_PROMPT + topic)
        st.write(answer)