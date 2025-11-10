import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download(['punkt', 'stopwords', 'wordnet'])
nltk.download('averaged_perceptron_tagger_eng')
from nltk import pos_tag

text = "Social network analysis focuses on studying interactions among users online."

words = word_tokenize(text)
filtered = [word for word in words if word not in stopwords.words('english') and word.isalpha()]

print(words)
print(filtered)

stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in filtered]
print(stemmed)

lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(word) for word in filtered]

print(lemmatized)

postag = pos_tag(filtered)

print(postag)
