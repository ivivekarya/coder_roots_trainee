import streamlit as st
from streamlit_option_menu import option_menu
import speech_recognition as sr

# Page config
st.set_page_config(page_title="VIVI HERE", layout="wide")
st.title("🚀 VIVI HERE")
if "input_toggle" not in st.session_state:
    st.session_state.input_toggle = True

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        "Menu",
        ["🏠 Home", "📞 Contact"],
        icons=["house", "telephone"],
        menu_icon="cast",
        default_index=0,
    )

# Chat logic
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

def handle_send():
    msg = st.session_state.user_input
    if msg:
        st.session_state.chat_history.append(("user", msg))
        if "hello" in msg.lower():
            reply = "Hello! 👋"
        elif "how are you" in msg.lower():
            reply = "I'm great! Thanks for asking 😊"
        else:
            reply = "I'm just a bot, still learning!"
        st.session_state.chat_history.append(("bot", reply))
        st.session_state.user_input = ""  # Clear input

if st.session_state.get("mic_triggered", False):
    handle_send()
    st.session_state.mic_triggered = False  # Reset so it only triggers once



# Home Section
if selected == "🏠 Home":
    st.title("💬 Chat with Me!")

    # Display chat history
    for sender, message in st.session_state.chat_history:
        if sender == "user":
            st.markdown(f"**🧑 You:** {message}")
        else:
            st.markdown(f"**🤖 Bot:** {message}")


            # Input + Send + Mic in a row
    key_name = "user_input1" if st.session_state.input_toggle else "user_input2"

    # Handle mic text injection & auto-send
    if "mic_text" in st.session_state:
        st.session_state[key_name] = st.session_state.mic_text
        st.session_state.user_input = st.session_state.mic_text
        del st.session_state["mic_text"]

        if st.session_state.get("send_after_mic"):
            handle_send()
            st.session_state["send_after_mic"] = False


    col1, col2, col3 = st.columns([6, 1, 1])
    with col1:
        st.text_input(
            "Your message:",
            key=key_name,
            placeholder="Type your message and press Enter...",
            label_visibility="collapsed",
            on_change=handle_send
        )

    
    with col2:
        if st.button("📤 Send"):
            st.session_state.user_input = st.session_state[key_name]
            handle_send()

    
    with col3:
        if st.button("🎤"):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                st.info("🎙️ Listening...")
                audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                st.success("✅ You said: " + said)
            except sr.UnknownValueError:
                st.warning("❗Could not understand audio")
            except sr.RequestError as e:
                st.error(f"⚠️ Could not request results; {e}")

            # Set user input directly and trigger handler on rerun
            st.session_state.user_input = said
            st.session_state["mic_triggered"] = True
            st.rerun()

# Contact Section
elif selected == "📞 Contact":
    st.title("📬 Get in Touch")
    st.text_input("Your Name")
    st.text_input("Email")
    st.text_area("Message")
    st.button("Send")
