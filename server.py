"""
Server module for the Emotion Detector application.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the text from the UI and returns emotion scores.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Handle empty input
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    try:
        response = emotion_detector(text_to_analyze)

        # Handle API returning invalid/None values
        if not response or response.get('dominant_emotion') is None:
            return "Invalid text! Please try again!"

        # Normal response
        return (
            f"For the given statement, the system response is "
            f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, 'joy': {response['joy']} and "
            f"'sadness': {response['sadness']}. The dominant emotion is "
            f"<b>{response['dominant_emotion']}</b>."
        )

    except (ValueError, KeyError, TypeError):
        # Catch specific processing errors
        return "Error occurred while processing the request. Please try again later."

@app.route("/")
def render_index_page():
    """
    Renders the main application page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006)
