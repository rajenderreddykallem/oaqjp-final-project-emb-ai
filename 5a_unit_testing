import unittest

from EmotionDetection import emotion_detector

class TestSquareFunction(unittest.TestCase):
    def test_emotion_detector(self):
        text_to_analyze = "I am tired today!"
        result = emotion_detector(text_to_analyze)
        self.assertIn('dominant_emotion', result)
        self.assertEqual(result['dominant_emotion'], 'sadness') 




unittest.main()

