import streamlit as st

st.title("LejonBot 🤖")

user_input = st.text_input("Say something")

if user_input:
    st.write("You said:", user_input)
    st.write("LejonBot: Nice! Tell me which course you're interested in 😊")
