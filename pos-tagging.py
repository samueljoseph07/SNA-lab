# install library - pip install nltk
import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "John is learning Natural Language Processing using Python and NLTK"
tokens = word_tokenize(text)
pos_tag_result = pos_tag(tokens)

print(pos_tag_result)
