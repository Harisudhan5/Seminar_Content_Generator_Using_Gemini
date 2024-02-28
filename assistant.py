from dotenv import load_dotenv
import time 
import streamlit as st
import os
import google.generativeai as ggi
load_dotenv(".env")

fetched_api_key = os.getenv("API_KEY")
ggi.configure(api_key = fetched_api_key)

model = ggi.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
def LLM_Response(question):
    response = chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title = "Generator")

st.header("Course Content Generator")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Enter the Tech stack for which you want to create Notes: ",key="input")
prompt = f"""Prompt : Give a course content for {input} in the format as follows: : 
Title : An Introduction Section on {input}

Introduction : 
6 lines in the introduction on what is the tech stack and its history

Why this tech stack :
10 points on why we need to learn the tech stack  

Demo :
Give a code for basic to demontrate the tech stack
"""

input = prompt
submit=st.button("Ask the question")

if submit and input:
    st.subheader("Generated Script : ")
    response = LLM_Response(input)
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.sidebar.title('Chat History')#    
for role, text in st.session_state['chat_history']:
    st.sidebar.subheader(f"{role}: {text}")
    



    
