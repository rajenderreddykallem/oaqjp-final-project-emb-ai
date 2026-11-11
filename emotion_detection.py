""" Emotion Detection App """

import requests 


def emotion_detector(text_to_analyze):
    """ Emotion detection function """
    
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input = { "raw_document": { "text": text_to_analyze } }
    text = requests.post(URL, json=Input, headers=Headers)
    
    print("Status Code:", text.status_code)
    #print("Response Body:", text.json())
    response = text.json()
    if text.status_code== 200:
        
        anger_score= response['emotionPredictions'][0]['emotionMentions'][0]['emotion']['anger']
        disgust_score= response['emotionPredictions'][0]['emotionMentions'][0]['emotion']['disgust']
        fear_score= response['emotionPredictions'][0]['emotionMentions'][0]['emotion']['joy']
        joy_score= response['emotionPredictions'][0]['emotionMentions'][0]['emotion']['fear']
        sadness_score= response['emotionPredictions'][0]['emotionMentions'][0]['emotion']['sadness']
        scores = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score}
        emotion = max(scores, key=scores.get)
        

        
        response_data = dict(anger=anger_score,disgust=disgust_score,fear=fear_score,joy=joy_score,sadness=sadness_score,dominant_emotion=emotion)
        return response_data
        
       

    return text 

