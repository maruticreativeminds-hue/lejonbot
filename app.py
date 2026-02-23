import streamlit as st

st.title("LejonBot 🤖")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Say something")

if user_input:
    st.session_state.messages.append(("You", user_input))

    reply = "Nice 🙂 Tell me which course you're interested in:\n\n"
    reply += "🎬 Animation\n🎨 Background Design\n✨ VFX\n🎞 Video Editing\n🤖 AI Film Making"

    st.session_state.messages.append(("LejonBot", reply))

for sender, msg in st.session_state.messages:
    st.write(f"**{sender}:** {msg}")
