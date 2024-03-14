import streamlit as st
import speech_recognition
from time import sleep
import json
from streamlit_lottie import st_lottie

container = st.container()
try:
    with container:
        @st.cache_data(ttl=60 * 60) # to store the lottie function data for one - hour in cache memory
        def load_lottie_file(filepath : str):
            with open(filepath, "r") as f: # opening  file in read mode
                gif = json.load(f) # load the json file
            st_lottie(gif, speed=1, width=650, height=450) # to display lottie image using st_lottie
                
        load_lottie_file("robot.json")
except:
    print("Don't raise exception") # if any exception arises then it goes  inside this condition and prints Don't raise exception

st.title("Speech to text converter chatbot 🤖")
st.warning("**Note**: the loop will runs infinitely until your speech recognize by the recognizer")

dic = {"Hindi":"hi-IN" , "English-india":"en-in" , "English-USA":"en-US" , "English-United Kingdom":"en-GB","tamil":"ta-IN"}
lang = st.selectbox("select language to transribe english to your selected language: ",list(dic.keys()))

def takeCommand():
    """
    Initializes a speech recognizer (r) and sets up microphone access.

    Prints "Listening..." to indicate the start of listening for speech.

    Adjusts recognition parameters:
        r.pause_threshold = 1: Allows up to 1 second of silence before considering speech complete.
        r.energy_threshold = 300: Sets the minimum audio energy level for speech detection.
    
    Listens for 4 seconds of audio from the microphone and stores it in the audio variable."""

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
            query = r.recognize_google(audio,language = dic[lang])
            sleep(0.5)
            with st.chat_message("assistant"):
                st.markdown(f"you said : {query}")
        except Exception as e:
            print("Say that again")
            return takeCommand() # if any mistake happens then recursive function will call again...
        return query # if it understands then it returns output

but = st.button("click here to listen...",use_container_width=True)
if but:
    takeCommand()
        
