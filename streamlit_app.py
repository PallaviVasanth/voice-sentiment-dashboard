import streamlit as st
from textblob import TextBlob
import speech_recognition as sr
import tempfile

st.title("Voice Sentiment Analyzer")

audio_file = st.file_uploader("Upload voice file", type=["wav"])

if audio_file is not None:
    # Save file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_file.read())
        temp_path = temp_audio.name

    r = sr.Recognizer()

    with sr.AudioFile(temp_path) as source:
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
