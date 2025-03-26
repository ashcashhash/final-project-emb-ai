"""
Flask application for emotion detection using EmotionDetection module.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)  # Best practice: Use __name__ instead of string

@app.route("/emotionDetector")
def emo_detector():
    """
    Endpoint to detect emotions from the provided text.
    Expects 'textToAnalyze' as a query parameter.
    """
    text_to_analyze = request.args.get('textToAnalyze', '')

    if not text_to_analyze:
        return "Invalid input! Please provide a valid text."

    response = emotion_detector(text_to_analyze)

    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is: "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']}, "
        f"and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the index.html page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
