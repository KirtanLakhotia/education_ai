import os
os.environ['OPENAI_API_KEY']="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"
from langchain.llms import OpenAI
llm1 = OpenAI(temperature = 0.7)

from langchain.prompts import PromptTemplate

english=PromptTemplate(
    input_variables=['a'],
    template="you are bad mafia tell me about {a} use double meaning words "  
)
hindi=PromptTemplate(
    input_variables=['a'],
    template="tell me only in hindi, text output should also be hindi about {a} use double meaning words "  
)
from langchain.chains import LLMChain

chain_english=LLMChain(llm=llm1,prompt=english)
chain_hindi=LLMChain(llm=llm1,prompt=hindi)


from gtts import gTTS
from IPython.display import Audio
import io  # Make sure you import the io module

def text_to_speech_english(text):
    language = 'en'  # English, change it to another language if you want!

    # Passing the text and language to the engine
    speech = gTTS(text=text, lang=language, slow=False,)
    speech.save("example_english.mp3")
    return
def text_to_speech_hindi(text):
    language = 'hi'  # English, change it to another language if you want!

    # Passing the text and language to the engine
    speech = gTTS(text=text, lang=language, slow=False,)
    speech.save("example_hindi.mp3")
    return

    # Save to BytesIO object
    # with io.BytesIO() as f:
    #     speech.write_to_fp(f)
    #     f.seek(0)
    #     audio = Audio(f.read(), autoplay=True)

    # return audio


# # Text to convert to speech
# a=input()
# output=chain.run(a)
# # print(output)
# audio_output = text_to_speech(output)


import streamlit as st

nav=st.sidebar.radio("NAVIGATION",["HOME","ABOUT","FURTURE"])
if nav=="HOME":
    nav_in_home=st.sidebar.radio("CHOOSE THE LANGUAGE",["ENGLISH","HINDI"])
    if nav_in_home=="ENGLISH":
        st.title("ASK ME ANYTHING, I AM YOUR STUDY HELPER")
        input_english=st.text_input("TYPE ANY TOPIC YOU WANT TO KNOW")
        if input_english:
           input=chain_english.run(input_english)
           st.write(input)
           text_to_speech_english(input)
           st.audio("example_english.mp3")


    if nav_in_home=="HINDI":
        st.title("ASK ME ANYTHING, I AM YOUR STUDY HELPER")
        input_hindi=st.text_input("KOI BHEE VISHAY MUJ SE PUCHO JO APP JANNAY CHATE HO")
        if input_hindi:
           input=chain_hindi.run(input_hindi)
           st.write(input)
           text_to_speech_hindi(input)
           st.audio("example_hindi.mp3")   


# ABOUT SECTION
if nav=="ABOUT":
    st.write("# Empowering Tomorrow with Intelligent Innovation: Your Future, Our Code.")
    st.image("WhatsApp Image 2023-08-05 at 11.26.43 PM.jpeg",width=650)
    st.snow()

# FURTURE SECTION
if nav=="FURTURE":
    st.write("# IN THE PRESENT MOMENT, WE CRAFT OUR PATH WITHOUT CONSTRAINING OUR THOUGHTS TO THE UNPREDICTABLE FUTURE. OUR ACTIONS ARE ROOTED IN TODAY, SHAPING OUR REALITY WITH INTENTION AND PURPOSE.")
    st.markdown("""# :sunglasses: :heart: :heart: :heart: :heart: :sunglasses: """)
    st.balloons()