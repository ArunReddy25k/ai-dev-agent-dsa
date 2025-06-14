import streamlit as st
from openai import OpenAI

# Streamlit config
st.set_page_config(page_title="AI Dev Agent", layout="wide")

st.title("🧠 AI Developer Agent + DSA Solver")
st.markdown("Ask me to write code, debug programs, or solve DSA problems in any programming language!")

# Input OpenAI API key
api_key = st.text_input("🔑 Enter your OpenAI API Key", type="password")
if not api_key:
    st.warning("Please enter your OpenAI API key to use this agent.")
    st.stop()

# Prompt input
prompt = st.text_area("📝 What do you want help with?", height=200)

# On button click
if st.button("🚀 Submit"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Thinking..."):
            try:
                # Use new OpenAI SDK
                client = OpenAI(api_key=api_key)

                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )

                answer = response.choices[0].message.content
                st.success("✅ Response:")
                st.code(answer, language='python')

            except Exception as e:
                st.error(f"❌ Error: {e}")
