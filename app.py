from flask import Flask, render_template, request, jsonify
from VoicetoText import record_and_transcribe
from BasicSentimentLogic import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the main dashboard page.
    """
    return render_template('index.html')

@app.route('/record', methods=['POST'])
def record():
    """
    Handles the recording request: transcribes speech and analyzes sentiment.
    Returns JSON with detected text and sentiment result.
    """
    text = record_and_transcribe()
    sentiment = analyze_sentiment(text)
    return jsonify({'text': text, 'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)  # Run in debug mode for development