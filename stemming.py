import nltk
nltk.download('punkt') #use punkt_tab if not working
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()
text = "The children are playing happily in the playground"
words = word_tokenize(text)
stem_words = [stemmer.stem(word) for word in words]
print(words)
print(stem_words)
