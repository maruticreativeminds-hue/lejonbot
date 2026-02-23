import streamlit as st
import time

st.set_page_config(page_title="LejonBot", page_icon="🤖")

st.title("LejonBot 🤖")

# ---------------- MEMORY ----------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to Lejon Animation Studio 😊 How can I help you today?"}
    ]

# ---------------- REPLY ENGINE ----------------
def reply_engine(text):
    text = text.lower()

    if "drawing" in text:
        return "🎨 Not at all 😊 Drawing skills are NOT required. We teach from basics."

    if "fees" in text:
        return "💰 Fees vary by course and duration. Please contact the studio for exact details."

    if "location" in text:
        return "📍 We are located at University Road, Rajkot."

    if "animation" in text:
        return "🎬 Animation Course includes 2D, 3D, character design & storytelling."

    return "Nice 🙂 You can ask about courses, fees, duration, or careers."

# ---------------- CHAT DISPLAY ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- QUICK ACTIONS (LIKE REAL CHAT) ----------------
st.write("")

c1, c2, c3 = st.columns(3)

if c1.button("🎬 Courses"):
    st.session_state.messages.append(
        {"role": "assistant", "content": "We offer:\n\n• Animation\n• VFX\n• Background Design\n• Video Editing\n• AI Film Making ✨"}
    )
    st.rerun()

if c2.button("💰 Fees"):
    st.session_state.messages.append(
        {"role": "assistant", "content": reply_engine("fees")}
    )
    st.rerun()

if c3.button("📍 Location"):
    st.session_state.messages.append(
        {"role": "assistant", "content": reply_engine("location")}
    )
    st.rerun()

# ---------------- USER INPUT ----------------
prompt = st.chat_input("Type your message")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("LejonBot typing..."):
            time.sleep(0.4)
            response = reply_engine(prompt)
            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
