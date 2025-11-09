from textblob import TextBlob
reviews = [
    "the product quality is excellent and I love it.",
    "Worst experience ever. Totally disappointed",
    "Average performance, could be better.",
    "beautiful but awful"
]

for review in reviews:
    blob = TextBlob(review)
    print("Review: ", review)
    print("Sentiment polarity: ", blob.sentiment.polarity)
    print("Sentiment type: ", 'Positive' if blob.sentiment.polarity>0 else 'Negative' if blob.sentiment.polarity<0 else 'neutral')
    print("-"*50)
