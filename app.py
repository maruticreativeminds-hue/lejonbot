import streamlit as st
import time

st.set_page_config(page_title="LejonBot", page_icon="🤖")

st.title("LejonBot 🤖")

# ---------------- MEMORY INIT ----------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to Lejon Animation Studio 😊 How can I help you today?"}
    ]

# ---------------- RESPONSE ENGINE ----------------
def generate_reply(user_text):
    text = user_text.lower()

    if any(word in text for word in ["hi", "hello", "hey"]):
        return "Hello 😊 Ask me about courses, fees, duration, drawing skills, or careers."

    elif "course" in text:
        return "We offer Animation, VFX, Background Design, Video Editing, and AI Film Making ✨"

    elif "animation" in text or "ani" in text:
        return "Great choice 😃 Our Animation program covers 2D, 3D, character design, and storytelling."

    elif "fees" in text or "fee" in text:
        return "Fees vary by course 🙂 For accurate details, please contact Lejon Animation Studio."

    elif "duration" in text:
        return "Duration depends on the selected program 👍 Typically ranges from short-term to professional tracks."

    elif "drawing" in text:
        return "No worries 😊 Drawing skills are NOT mandatory. We train from basics."

    elif "career" in text or "job" in text:
        return "Students explore careers in animation studios, VFX houses, gaming, editing, and digital media 🚀"

    elif "location" in text:
        return "We are located at 📍 University Road, Rajkot."

    else:
        return "Nice 🙂 You can ask about courses, fees, duration, drawing skills, careers, or location."

# ---------------- CHAT HISTORY RENDER ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- USER INPUT ----------------
user_prompt = st.chat_input("Type your message")

if user_prompt:

    # store user message
    st.session_state.messages.append(
        {"role": "user", "content": user_prompt}
    )

    with st.chat_message("user"):
        st.markdown(user_prompt)

    # typing indicator (feels real)
    with st.chat_message("assistant"):
        with st.spinner("LejonBot is typing..."):
            time.sleep(0.6)
            reply = generate_reply(user_prompt)
            st.markdown(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

# ---------------- QUICK REPLY BUTTONS ----------------
st.write("")

col1, col2, col3 = st.columns(3)

if col1.button("🎬 Courses"):
    st.session_state.messages.append({"role": "assistant", "content": generate_reply("courses")})
    st.rerun()

if col2.button("💰 Fees"):
    st.session_state.messages.append({"role": "assistant", "content": generate_reply("fees")})
    st.rerun()

if col3.button("📍 Location"):
    st.session_state.messages.append({"role": "assistant", "content": generate_reply("location")})
    st.rerun()
