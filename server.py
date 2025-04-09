from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection  import emotion_detector 
app = Flask("Emotion Detector")
@app.route("/emotionDetector", methods=['POST'])
def emo_analyzer():   
    data = request.json
    statement = data.get("statement", "")   
    result = emotion_detector(statement)    
    output_message = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )    
    return jsonify(result=result, message=output_message)
@app.route("/")
def render_index_page():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)