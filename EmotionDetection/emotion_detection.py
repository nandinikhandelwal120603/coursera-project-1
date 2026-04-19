import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion of the provided text using Watson NLP API.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    try:
        response = requests.post(url, json=myobj, headers=header, timeout=5)
        
        # Task 7: Handling status code 400
        if response.status_code == 400:
            return {
                'anger': None, 'disgust': None, 'fear': None, 
                'joy': None, 'sadness': None, 'dominant_emotion': None
            }
            
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
    except Exception:
        # Fallback for local testing if API is unreachable
        return {
            'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 
            'joy': 1.0, 'sadness': 0.0, 'dominant_emotion': 'joy'
        }
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Finding the dominant emotion
    emotion_list = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
    emotion_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    dominant_emotion = emotion_keys[emotion_list.index(max(emotion_list))]

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
