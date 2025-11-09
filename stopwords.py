import nltk
nltk.download('stopwords')
nltk.download('punkt') # use punkt_tab if not working
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "This is an example showing how to remove stopwords"
words = word_tokenize(text)
stopwords = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stopwords]

print(words)
print(filtered_words)
