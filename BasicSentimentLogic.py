from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text using TextBlob.
    Returns 'Positive', 'Negative', or 'Neutral' based on polarity.
    """
    if not text or text.startswith("Could not") or text.startswith("No speech") or text.startswith("Speech recognition"):
        return "Error"  # If text is an error message, return "Error"
    
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Polarity ranges from -1 (negative) to 1 (positive)
    
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"