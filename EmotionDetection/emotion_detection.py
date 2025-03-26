import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    output = {}
    # If the response status code is 200
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        output = formatted_response['emotionPredictions'][0]['emotion']
        output["dominant_emotion"] = max(output, key=output.get)
    # If the response status code is anything apart from 200
    else:
        output['anger'] = None
        output['disgust'] = None
        output['fear'] = None
        output['joy'] = None
        output['sadness'] = None
        output['dominant_emotion'] = None
    return output