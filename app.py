import streamlit as st
import cohere
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# ✅ Debugging - Check if the API key is loaded
if not COHERE_API_KEY:
    st.error("Cohere API Key not found. Please check your .env file.")
else:
    st.success("API Key Loaded Successfully")

# Initialize Cohere client
co = cohere.Client(COHERE_API_KEY)

# Streamlit UI
st.title("🤖 Cohere Chatbot")
st.markdown("Ask anything and get intelligent responses powered by Cohere's AI.")

# Input area for questions
question = st.text_area("Enter your question:", height=150)

# Button to trigger API call
if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question to ask.")
    else:
        with st.spinner("Generating response..."):
            try:
                response = co.chat(
                    model='command-xlarge-nightly',
                    message=question,   # <--- Fixed this parameter
                    temperature=0.5
                )
                st.success("Response:")
                st.write(response.text.strip())
            except Exception as e:
                st.error(f"Error: {str(e)}")
