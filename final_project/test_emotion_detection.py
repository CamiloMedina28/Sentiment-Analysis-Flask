import unittest 
import EmotionDetection as emdetect

class TestEmotions(unittest.TestCase):
    def test_joy(self):
        ans = emdetect.emotion_detector.emotion_detector("I am glad this happened")
        result = emdetect.format_output.format_output(ans)
        self.assertEqual(result[0], 'joy')

    def test_anger(self):
        ans = emdetect.emotion_detector.emotion_detector("I am really mad about this")
        result = emdetect.format_output.format_output(ans)
        self.assertEqual(result[0], 'anger')

    def test_disgust(self):
        ans = emdetect.emotion_detector.emotion_detector("I feel disgusted just hearing about this")
        result = emdetect.format_output.format_output(ans)
        self.assertEqual(result[0], 'disgust')

    def test_sadness(self):
        ans = emdetect.emotion_detector.emotion_detector("I am so sad about this")
        result = emdetect.format_output.format_output(ans)
        self.assertEqual(result[0], 'sadness')

    def test_fear(self):
        ans = emdetect.emotion_detector.emotion_detector("I am really afraid that this will happen fear")
        result = emdetect.format_output.format_output(ans)
        self.assertEqual(result[0], 'fear')    

if __name__ == '__main__':
    unittest.main()