# Import necessary libraries
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download necessary NLTK data (VADER lexicon)
nltk.download('vader_lexicon')

# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Sample text
text = "I love this product! It's absolutely amazing and works great."

# Perform sentiment analysis
sentiment_score = sia.polarity_scores(text)

# Output the sentiment score
print(f"Sentiment scores: {sentiment_score}")

# Interpret the sentiment
compound_score = sentiment_score['compound']

if compound_score >= 0.05:
    sentiment = "Positive"
elif compound_score <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print(f"Overall sentiment: {sentiment}")
