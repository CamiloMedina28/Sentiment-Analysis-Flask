import requests
def emotion_detector(text_to_analyse: str) -> str:
    """
    Function to detect emotions using Watson NLP Library 

    Args
    ----
    text_to_analyse(str): Text to obtain emotions

    Return
    ------
    ans.text(str): Returns the emotion analysis in a string
    """
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"Grpc-Metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    ans = requests.post(URL, json = input_json, headers = Headers)
    if ans.status_code == 400:
        ans = {'anger': None,
                'disgust': None, 
                'fear': None, 
                'joy': None, 
                'sadness': None}
    else: 
        return ans.text
        