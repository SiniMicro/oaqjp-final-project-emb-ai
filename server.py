"""
This is the Flask server for analyzing the emotions in a given text statement.
It exposes two routes:
1. /emotionDetector: Analyzes a given statement for emotions and returns the results.
2. /: Renders the index.html page of the application.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

# Initialize Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=['POST'])
def emo_analyzer():
    """
    Analyzes the emotional content of a given statement.

    This function takes a JSON object with a "statement" key, processes it with
    the emotion detector, and returns the emotional analysis along with a message.
    If no valid emotion is detected, it returns an error message.

    Args:
        None

    Returns:
        jsonify: A JSON response containing emotion analysis and a message.
    """
    # Retrieve the statement from the request
    data = request.json
    statement = data.get("statement", "")

    # Get emotion analysis for the statement
    result = emotion_detector(statement)

    if result['dominant_emotion'] is None:  # Check if the dominant emotion is None
        output_message = "Invalid text! Please try again!"
        return jsonify(result=result, message=output_message)

    # Prepare the output message if valid emotions are detected
    output_message = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return jsonify(result=result, message=output_message)

@app.route("/")
def render_index_page():
    """
    Renders the index HTML page.

    This route serves the main page of the application where users can input text 
    for emotion analysis.

    Args:
        None

    Returns:
        render_template: The rendered index.html page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    """
    Runs the Flask application on host 0.0.0.0 and port 5005.

    Args:
        None

    Returns:
        None
    """
    # Run the app
    app.run(host="0.0.0.0", port=5005)
