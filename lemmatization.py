import nltk
nltk.download('punkt') #use punkt_tab if not working
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()
text = "The children are playing happily with their friends"
words = word_tokenize(text)
lemmwords = [lemmatizer.lemmatize(word) for word in words]

print(words)
print(lemmwords)
