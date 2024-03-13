import streamlit as st
import speech_recognition
from time import sleep
import json
from streamlit_lottie import st_lottie

container = st.container()
try:
    with container:
        @st.cache_data(ttl=60 * 60)
        def load_lottie_file(filepath : str):
            with open(filepath, "r") as f:
                gif = json.load(f)
            st_lottie(gif, speed=1, width=650, height=450)
                
        load_lottie_file("robot.json")
except:
    print("Don't raise exception")
st.title("Speech to text converter chatbot 🤖")
st.warning("**Note**: the loop will runs infinitely until your speech recognize by the recognizer")
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source,0,4)

        try:
            with st.chat_message("assistant"):
                st.markdown("Listening...")
            sleep(0.5)
            with st.chat_message("assistant"):
                st.markdown("understanding...")
            query = r.recognize_google(audio,language = "en-in")
            sleep(0.5)
            with st.chat_message("assistant"):
                st.markdown(f"you said : {query}")
        except Exception as e:
            print("Say that again")
            return takeCommand()
        return query

but = st.button("click here to listen...",use_container_width=True)
if but:
    takeCommand()
        
