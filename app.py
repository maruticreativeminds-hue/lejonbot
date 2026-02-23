import streamlit as st
import time

st.set_page_config(page_title="LejonBot", page_icon="🤖")

st.title("LejonBot 🤖")

# ---------------- MEMORY INIT ----------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to Lejon Animation Studio 😊 How can I help you today?"}
    ]

if "active_panel" not in st.session_state:
    st.session_state.active_panel = None

# ---------------- RESPONSE ENGINE ----------------
def generate_reply(user_text):
    text = user_text.lower()

    if "animation" in text:
        return "🎬 Animation Course: Covers 2D, 3D, character design & storytelling."

    elif "vfx" in text:
        return "✨ VFX Course: Learn visual effects, compositing & cinematic visuals."

    elif "editing" in text:
        return "🎞 Video Editing: Professional editing, transitions & production workflow."

    return "Nice choice 👍 Ask anything else!"

# ---------------- CHAT RENDER ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- USER INPUT ----------------
prompt = st.chat_input("Type your message")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("LejonBot is typing..."):
            time.sleep(0.5)
            reply = generate_reply(prompt)
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

# ---------------- MAIN ACTION BUTTONS ----------------
st.write("")
col1, col2, col3 = st.columns(3)

if col1.button("🎬 Courses"):
    st.session_state.active_panel = "courses"
    st.rerun()

if col2.button("💰 Fees"):
    st.session_state.active_panel = "fees"
    st.rerun()

if col3.button("📍 Location"):
    st.session_state.active_panel = "location"
    st.rerun()

# ---------------- DYNAMIC PANELS ----------------
st.write("")

if st.session_state.active_panel == "courses":
    st.subheader("Choose a Course")

    c1, c2, c3 = st.columns(3)

    if c1.button("Animation"):
        st.session_state.messages.append({"role": "assistant", "content": generate_reply("animation")})
        st.rerun()

    if c2.button("VFX"):
        st.session_state.messages.append({"role": "assistant", "content": generate_reply("vfx")})
        st.rerun()

    if c3.button("Editing"):
        st.session_state.messages.append({"role": "assistant", "content": generate_reply("editing")})
        st.rerun()

elif st.session_state.active_panel == "fees":
    st.subheader("Fees Information")
    st.info("💰 Fees vary by course and duration. Please contact Lejon Animation Studio for exact details.")

elif st.session_state.active_panel == "location":
    st.subheader("Studio Location")
    st.success("📍 University Road, Rajkot")
