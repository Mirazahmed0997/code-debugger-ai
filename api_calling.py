from google import genai
from dotenv import load_dotenv
import os,io
import streamlit as st
from gtts import gTTS


load_dotenv()

api_key= os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)

def text_generator(text):
    
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=text,
    )

    return(response.text)


def generate_solution(images,selected_option):
    
    prompt=f"""Generate solution based on {selected_option},
     if user need hint give him spme hint how he can resolve the bug in his system ,
     or if user choose code give him the full code,
    make sure to add markdown,"""
    response=client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[images,prompt],
   )
    return response.text
