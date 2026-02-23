import streamlit as st

st.set_page_config(page_title="LejonBot", page_icon="🤖")

st.title("LejonBot 🤖")

# ---- Memory Init ----
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "text": "Welcome to Lejon Animation Studio 😊 How can I help you today?"}
    ]

# ---- Input Box FIRST (important) ----
user_input = st.chat_input("Type your message")

# ---- Process Input ----
if user_input:
    st.session_state.messages.append({"role": "user", "text": user_input})
    text = user_input.lower()

    if any(word in text for word in ["hi", "hello", "hey"]):
        reply = "Hello 😊 You can ask about courses, fees, duration, drawing, or careers."

    elif "course" in text:
        reply = "We offer Animation, VFX, Background Design, Video Editing, and AI Film Making ✨"

    elif "animation" in text or "ani" in text:
        reply = "Great choice 😃 Animation includes 2D, 3D, character design & storytelling."

    elif "fees" in text or "fee" in text:
        reply = "Fees vary by course 🙂 Please contact the studio for details."

    elif "duration" in text:
        reply = "Duration depends on the selected program 👍"

    elif "drawing" in text:
        reply = "No worries 😊 Drawing skills are NOT required."

    elif "location" in text:
        reply = "We are located at 📍 University Road, Rajkot."

    else:
        reply = "Nice 🙂 Ask me about courses, fees, duration, drawing, or careers."

    st.session_state.messages.append({"role": "bot", "text": reply})

# ---- Chat Display AFTER processing ----
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["text"])
    else:
        with st.chat_message("assistant"):
            st.write(msg["text"])
