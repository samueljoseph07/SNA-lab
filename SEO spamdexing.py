import nltk
from collections import Counter
from nltk.tokenize import word_tokenize
text = "cheap flights cheap tickets cheap hotels cheap packages cheap deals"
tokens = word_tokenize(text)
count = Counter(tokens)
for word, freq in count.items():
    if freq/len(tokens) > 0.3:
        print("Potential spam word: ", word)
