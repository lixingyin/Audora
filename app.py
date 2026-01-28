import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import time
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# functions 
def generate_album_art(user_prompt):
    if not user_prompt:
        return "Please provide a valid prompt."
    
    response = client.images.generate(
                model = "dall-e-3",
                prompt = user_prompt,
                size = "1024x1024",
                quality = "standard",
                n = 1,
    )

    image_url = response.data[0].url
    st.image(image_url, caption=f"Generated: {user_prompt}")

# main app
st.title("Audora")
st.write("Welcome to Audora! This is a simple app that uses OpenAI's API.")

with st.form("mood_form", clear_on_submit=True):
    prompt = st.text_input("Enter your prompt:")
    submitted = st.form_submit_button("Submit")

    if submitted and prompt:
        success_message = st.empty()

        success_message.text("Generating response...")

        generate_album_art(prompt)

        success_message.empty()


