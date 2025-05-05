import streamlit as st
import speech_recognition as sr
import pyttsx3
import openai

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Bol kya chahiye...")
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        st.write(f"Tune bola: {query}")
        return query
    except:
        speak("Sahi se bol bhai, samajh nahi aaya")
        return ""

def chatgpt_response(prompt):
    openai.api_key = "YOUR_API_KEY"  # Apna API key dalna
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def main():
    st.title("Voice Assistant with ChatGPT")

    # Get user input from button click
    if st.button("Start Listening"):
        user_input = listen()
        if "band kar" in user_input.lower():
            speak("Thik hai, milte hain baad mein.")
            st.write("Assistant stopped.")
        else:
            reply = chatgpt_response(user_input)
            speak(reply)
            st.write(f"ChatGPT ka response: {reply}")

if __name__ == "__main__":
    main()
