import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="LejonBot", page_icon="🤖")
st.title("LejonBot 🤖")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are LejonBot, assistant of Lejon Animation Studio in Rajkot. Reply friendly and helpful. If question unrelated, politely guide user to contact studio."}
    ]

for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Type your message")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.responses.create(
                model="gpt-5-mini",
                input=st.session_state.messages
            )
            reply = response.output_text
            st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
