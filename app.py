import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load env
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="GenAI Translator", layout="centered")

st.title("🌍 GenAI Language Translator")

# Inputs
text = st.text_area("Enter text to translate")

source_lang = st.selectbox(
    "Source Language",
    ["English", "Hindi", "Spanish", "French", "German", "Telugu"]
)

target_lang = st.selectbox(
    "Target Language",
    ["English", "Hindi", "Spanish", "French", "German", "Telugu"]
)

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        with st.spinner("Translating..."):
            prompt = f"""
            Translate the following text from {source_lang} to {target_lang}.
            Only return the translated text.

            Text: {text}
            """

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a professional translator."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )

            translated = response.choices[0].message.content

            st.subheader("Translated Text")
            st.success(translated)