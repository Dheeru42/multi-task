from textblob import TextBlob
import translate
blob = TextBlob("Buongiorno!")
blob.detect_language()