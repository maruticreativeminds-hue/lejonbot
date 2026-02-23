import streamlit as st

st.set_page_config(page_title="LejonBot", page_icon="🤖")

st.title("LejonBot 🤖")

# Memory initialization
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "text": "Welcome to Lejon Animation Studio 😊 How can I help you today?"}
    ]

# ---- INPUT FORM (CRITICAL FIX) ----
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message")
    submitted = st.form_submit_button("Send")

# ---- MESSAGE PROCESSING ----
if submitted and user_input:
    st.session_state.messages.append({"role": "user", "text": user_input})
    text = user_input.lower()

    if any(word in text for word in ["hi", "hello", "hey"]):
        reply = "Hello 😊 You can ask about courses, fees, duration, drawing, or careers."

    elif "course" in text:
        reply = (
            "We offer exciting courses ✨\n\n"
            "🎬 Animation\n"
            "🎨 Background Design\n"
            "✨ VFX\n"
            "🎞 Video Editing\n"
            "🤖 AI Film Making\n\n"
            "Which one interests you?"
        )

    elif "ani" in text:
        reply = "Great choice 😃 Animation covers 2D & 3D fundamentals, character design, and storytelling."

    elif "bg" in text or "background" in text:
        reply = "Nice 😍 Background Design teaches environment drawing, perspective, and digital painting."

    elif "vfx" in text:
        reply = "Awesome 🔥 VFX includes visual effects, compositing, and effects workflow."

    elif "edit" in text:
        reply = "Cool 🎬 Video Editing covers transitions, cinematic cuts, and editing tools."

    elif "ai" in text:
        reply = "Future-ready choice 🤖 AI Film Making explores modern AI tools for creative projects."

    elif any(word in text for word in ["fee", "fees", "price"]):
        reply = "Fees vary by course 🙂 Please contact the studio for complete details."

    elif any(word in text for word in ["duration", "how long", "length"]):
        reply = "Course duration depends on the program and learning pace 👍"

    elif "drawing" in text:
        reply = "No worries 😊 Drawing skills are NOT required. We teach everything from basics."

    elif any(word in text for word in ["location", "where", "address"]):
        reply = "We are located at 📍 University Road, Rajkot."

    elif any(word in text for word in ["job", "career", "future"]):
        reply = "Animation offers amazing career paths in films, games, design, and digital content ✨"

    else:
        reply = "Nice 🙂 Ask me about courses, fees, duration, drawing, or careers."

    st.session_state.messages.append({"role": "bot", "text": reply})
    st.rerun()

# ---- CHAT DISPLAY (AFTER LOGIC) ----
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"<div style='text-align:right; background:#0a84ff; color:white; padding:10px; border-radius:12px; margin:6px;'>"
            f"{msg['text']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='text-align:left; background:#1f2937; color:#00ffcc; padding:10px; border-radius:12px; margin:6px;'>"
            f"{msg['text']}</div>",
            unsafe_allow_html=True
        )
