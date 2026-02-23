import streamlit as st

st.title("LejonBot 🤖")

if "messages" not in st.session_state:
    st.session_state.messages = [
        ("LejonBot", "Welcome to Lejon Animation Studio 😃\n\nHow can I help you today?")
    ]

user_input = st.text_input("Say something")

if user_input:
    st.session_state.messages.append(("You", user_input))
    text = user_input.lower()

    if "hello" in text or "hi" in text:
        reply = "Hey there 😊 How can I help you? You can ask about courses, fees, duration, eligibility, etc."

    elif "course" in text or "courses" in text:
        reply = (
            "Here are our courses 🎬\n\n"
            "🎬 Animation\n"
            "🎨 Background Design\n"
            "✨ VFX\n"
            "🎞 Video Editing\n"
            "🤖 AI Film Making\n\n"
            "Which one interests you?"
        )

    elif "animation" in text:
        reply = (
            "Awesome choice 😃\n\nAnimation covers:\n"
            "• 2D & 3D Fundamentals\n"
            "• Character Design\n"
            "• Storytelling\n"
            "• Industry Workflow"
        )

    elif "background" in text:
        reply = (
            "Great pick 🎨\n\nBackground Design includes:\n"
            "• Environment Drawing\n"
            "• Perspective\n"
            "• Digital Painting"
        )

    elif "vfx" in text:
        reply = (
            "Nice 🔥\n\nVFX course teaches:\n"
            "• Visual Effects Basics\n"
            "• Compositing\n"
            "• Effects Workflow"
        )

    elif "editing" in text:
        reply = (
            "Cool 🎞\n\nVideo Editing covers:\n"
            "• Editing Software\n"
            "• Transitions\n"
            "• Cinematic Cuts"
        )

    elif "ai" in text:
        reply = (
            "Future-ready choice 🤖✨\n\nAI Film Making includes:\n"
            "• AI Tools\n"
            "• Content Creation\n"
            "• Modern Workflow"
        )

    elif "fee" in text or "fees" in text or "price" in text:
        reply = "Fees vary by course 🙂 Please contact the studio directly for latest details."

    elif "duration" in text or "how long" in text:
        reply = "Course duration depends on the program 👍 Typically discussed during counseling."

    elif "eligibility" in text or "who can join" in text:
        reply = (
            "Everyone is welcome 😃\n\n"
            "• School students\n"
            "• College students\n"
            "• Graduates\n"
            "• Beginners & advanced learners"
        )

    elif "drawing" in text or "not know drawing" in text:
        reply = "No worries at all 😊 Drawing skills are NOT required. We teach from basics."

    elif "location" in text or "where" in text or "address" in text:
        reply = "We are located at 📍 University Road, Rajkot."

    elif "contact" in text or "phone" in text or "call" in text:
        reply = "You can visit the studio directly on University Road, Rajkot 👍"

    else:
        reply = "Nice 🙂 You can ask me about courses, eligibility, fees, duration, or location."

    st.session_state.messages.append(("LejonBot", reply))

for sender, msg in st.session_state.messages:
    st.write(f"**{sender}:** {msg}")
