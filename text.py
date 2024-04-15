import streamlit as st
import speech_recognition
from time import sleep
import json
from streamlit_lottie import st_lottie
from deep_translator import GoogleTranslator

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

dic = {"Afrikaans":"af",
"Albanian":"sq",
"Amharic":"am",
"Arabic":"ar",
"Armenian":"hy",
"Assamese":"as",
"Aymara":"ay",
"Azerbaijani":"az",
"Bambara":"bm",
"Basque":"eu",
"Belarusian":"be",
"Bengali":"bn",
"Bhojpuri":"bho",
"Bosnian":"bs",
"Bulgarian":"bg",
"Catalan":"ca",
"Cebuano":"ceb",
"Chinese":"zh-CN", 
"Chinese":"zh-TW", 
"Corsican":"co",
"Croatian":"hr",
"Czech":"cs",
"Danish":"da",
"Dhivehi":"dv",
"Dogri":"doi",
"Dutch":"nl",
"English":"en",
"Esperanto":"eo",
"Estonian":"et",
"Ewe":"ee",
"Filipino":"fil",
"Finnish":"fi",
"French":"fr",
"Frisian":"fy",
"Galician":"gl",
"Georgian":"ka",
"German":"de",
"Greek":"el",
"Guarani":"gn",
"Gujarati":"gu",
"Haitian Creole":"ht",
"Hausa":"ha",
"Hawaiian":"haw",
"Hebrew":"he",
"Hindi":"hi",
"Hmong":"hmn",
"Hungarian":"hu",
"Icelandic":"is",
"Igbo":"ig",
"Ilocano":"ilo",
"Indonesian":"id",
"Irish":"ga",
"Italian":"it",
"Japanese":"ja",
"Javanese":"jv",
"Kannada":"kn",
"Kazakh":"kk",
"Khmer":"km",
"Kinyarwanda":"rw",
"Konkani":"gom",
"Korean":"ko",
"Krio":"kri",
"Kurdish":"ku",
"Kurdish(Sorani)":"ckb",
"Kyrgyz":"ky",
"Lao":"lo",
"Latin":"la",
"Latvian":"lv",
"Lingala":"ln",
"Lithuanian":"lt",
"Luganda":"lg",
"Luxembourgish":"lb",
"Macedonian":"mk",
"Maithili":"mai",
"Malagasy":"mg",
"Malay":"ms",
"Malayalam":"ml",
"Maltese":"mt",
"Maori":"mi",
"Marathi":"mr",
"Meiteilon(Manipuri)":"mni-Mtei",
"Mizo":"lus",
"Mongolian":"mn",
"Myanmar(Burmese)":"my",
"Nepali":"ne",
"Norwegian":"no",
"Nyanja(Chichewa)":"ny",
"Odia(Oriya)":"or",
"Oromo":"om",
"Pashto":"ps",
"Persian":"fa",
"Polish":"pl",
"Portuguese(Portugal, Brazil)":"pt",
"Punjabi":"pa",
"Quechua":"qu",
"Romanian":"ro",
"Russian":"ru",
"Samoan":"sm",
"Sanskrit":"sa",
"Scots Gaelic":"gd",
"Sepedi":"nso",
"Serbian":"sr",
"Sesotho":"st",
"Shona":"sn",
"Sindhi":"sd",
"Sinhala (Sinhalese)":"si",
"Slovak":"sk",
"Slovenian":"sl",
"Somali":"so",
"Spanish":"es",
"Sundanese":"su",
"Swahili":"sw",
"Swedish":"sv",
"Tagalog (Filipino)":"tl",
"Tajik":"tg",
"Tamil":"ta",
"Tatar":"tt",
"Telugu":"te",
"Thai":"th",
"Tigrinya":"ti",
"Tsonga":"ts",
"Turkish":"tr",
"Turkmen":"tk",
"Twi (Akan)":"ak",
"Ukrainian":"uk",
"Urdu":"ur",
"Uyghur":"ug",
"Uzbek":"uz",
"Vietnamese":"vi",
"Welsh":"cy",
"Xhosa":"xh",
"Yiddish":"yi",
"Yoruba":"yo",
"Zulu":"zu"}
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
            query = r.recognize_google(audio,language = "en-IN")
            translation = GoogleTranslator(source='en', target=dic[lang]).translate(query)
            
            sleep(0.5)
            with st.chat_message("assistant"):
                st.header(f"you said : {query}")
            with st.chat_message("assistant"):
                st.subheader(f"Translated text: {translation}")
        except Exception as e:
            print("Say that again")
            return takeCommand() # if any mistake happens then recursive function will call again...
        return query # if it understands then it returns output

but = st.button("click here to listen...",use_container_width=True)
if but:
    takeCommand()
        
