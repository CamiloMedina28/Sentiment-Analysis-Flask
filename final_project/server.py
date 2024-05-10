from flask import Flask, render_template, request
import EmotionDetection as emdetect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotion():
    text = request.args.get('textToAnalyze')
    ans = emdetect.emotion_detector.emotion_detector(text)
    result = emdetect.format_output.format_output(ans)
    if result[0] == "error":
        return result[1]
    else:
        return f"""For the given statement, the system response is 
                {result[1]}. The dominant emotion is {result[0]}."""


if __name__ == "__main__":
    app.run(port=8080, debug = True)
