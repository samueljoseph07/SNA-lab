import nltk
nltk.download('punkt') #use punkt_tab if not working
from nltk.tokenize import word_tokenize

text = "This is an example."
words = word_tokenize(text)

print(words)
