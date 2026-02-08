# Voice-Based Sentiment Analysis Dashboard using Flask and NLP

## Description
This is a simple web-based mini project that allows users to record voice input via their microphone, convert it to text, and analyze its sentiment (Positive, Negative, or Neutral). The results are displayed on a clean dashboard built with Flask.

## Features
- Voice recording from the system microphone.
- Speech-to-text conversion using SpeechRecognition.
- Sentiment analysis using TextBlob NLP.
- Web dashboard with a "Start Recording" button.
- Displays detected text and sentiment result.
- Graceful error handling for issues like no speech or unclear audio.
- Simple, responsive UI with dynamic updates via JavaScript.

## Technologies Used
- **Flask**: Web framework for the backend.
- **SpeechRecognition**: For audio recording and speech-to-text.
- **PyAudio**: For microphone access.
- **TextBlob**: For natural language processing and sentiment analysis.
- **HTML/CSS/JavaScript**: For the frontend dashboard.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`.
2. Run the app: `python app.py`.
3. Open `http://127.0.0.1:5000/` in your browser.
4. Click "Start Recording" and speak clearly.

## Functional Flow
1. User opens the webpage.
2. Clicks "Start Recording" → Microphone records audio.
3. Speech is converted to text.
4. Sentiment is analyzed.
5. Detected text and sentiment are displayed on the page.

## Notes
- Requires an internet connection for speech recognition.
- Ensure your microphone is enabled and permissions are granted.
- This is a beginner-friendly project; code is commented for clarity.