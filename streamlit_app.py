import streamlit as st
from textblob import TextBlob
import speech_recognition as sr

st.title("Voice Sentiment Analyzer")

audio_file = st.file_uploader("Upload voice file", type=["wav"])

if audio_file:
    r = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
        text = r.recognize_google(audio)

    st.write("Detected Text:", text)

    sentiment = TextBlob(text).sentiment.polarity

    if sentiment > 0:
        st.success("Positive")
    elif sentiment < 0:
        st.error("Negative")
    else:
        st.info("Neutral")

