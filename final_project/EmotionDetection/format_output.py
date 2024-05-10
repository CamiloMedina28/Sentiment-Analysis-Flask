import json

def format_output(answer:str) -> tuple:
    """
    Function that finds the emotion with the highest score and formats
    the dictionary with the scores

    Args
    ----
    answer(str): Unformated scores with emotions

    Returns
    -------
    tuple: Emotion with the highest score and formated dictionary.
    """
    try:
        json_format = json.loads(answer)
    except TypeError:
        return ("error", "<br>Invalid text! Please try again!</br>")
    else:
        emotions_dict = json_format['emotionPredictions'][0]['emotion']
        max_emotion = max(emotions_dict, key = emotions_dict.get)
        return (max_emotion, emotions_dict)

