import streamlit as st
from textblob import TextBlob

st.title("Voice Sentiment Analyzer")

st.write("Enter a sentence to analyze sentiment")

text = st.text_input("Type something...")

if st.button("Analyze"):
    if text:
        analysis = TextBlob(text)
        sentiment = analysis.sentiment.polarity

        if sentiment > 0:
            st.success("Positive 😊")
        elif sentiment < 0:
            st.error("Negative 😠")
        else:
            st.info("Neutral 😐")
    else:
        st.warning("Please enter text")
