import requests
import json
def emotion_detector(text_to_analyse):
    if not text_to_analyse.strip():  # Check for empty input
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)  
    if response.status_code == 400:  # Check if the response is bad
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    formatted_response = json.loads(response.text)   
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant_emotion
    return emotion_scores

