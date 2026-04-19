import google as genai
import os
from dotenv import load_dotenv
import streamlit as st
from api_calling import generate_solution
from api_calling import text_generator

from PIL import Image


load_dotenv()

st.title("Code Debugger")
st.markdown("Upload the screenshot")
st.divider()


with st.container(border=True):
        text=st.text_input("Ask anything to Miraz")
        if text:
            ans=text_generator(text)
            st.markdown(ans)


with st.sidebar:
        st.header("Controls")
        
        images = st.file_uploader(
            "Upload a image",
            type=["jpg","jpeg","png"],
            accept_multiple_files=False
            ) 
        
        
        
        
        
        
            
            
            
        if images:
             converted_image=Image.open(images)
     
    
    
    # options
    
        selected_option=st.selectbox("Select the difficulties",("Hints","Code"),index=None)

        submit_button=st.button("Submit",type="primary")

if submit_button:
    if not images:
        st.error("Need to upload an image")
    if not selected_option:
        st.error("Please select an option")
    if images and selected_option:
        
        with st.container(border=True):
            st.subheader(f"Debugging ({selected_option})")
            with st.spinner("Generating answer"):
                answer = generate_solution(converted_image,selected_option)
                st.markdown(answer)
        
            
            
            
        

