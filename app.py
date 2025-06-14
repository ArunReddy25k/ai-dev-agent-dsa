import streamlit as st
import openai
import os

# Streamlit page config
st.set_page_config(page_title="AI Dev Agent", layout="wide")

st.title("🧠 AI Developer Agent + DSA Solver")
st.markdown("Ask me to write code, debug programs, or solve DSA problems in any programming language!")

# API Key input or from env
api_key = st.text_input("🔑 Enter your OpenAI API Key", type="password")
if api_key:
    openai.api_key = api_key
else:
    st.warning("Please enter your OpenAI API key to use this agent.")
    st.stop()

# User prompt
prompt = st.text_area("📝 What do you want help with?", height=200)

if st.button("🚀 Submit"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful AI developer assistant. Answer as concisely as possible."},
                        {"role": "user", "content": prompt}
                    ]
                )
                answer = response['choices'][0]['message']['content']
                st.success("✅ Response:")
                st.code(answer, language='python')
            except Exception as e:
                st.error(f"❌ Error: {e}")
