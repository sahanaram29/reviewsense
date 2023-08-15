import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
import numpy as np
import module1 as t1
import settings
from settings import normalize

def sentiment():
    df = t1.rename_columns()
    sentiments = SentimentIntensityAnalyzer()
    # Create sentiment column
    sentiment_labels = []
    for review_text in df['reviews_text']:
        sentiment_scores = sentiments.polarity_scores(review_text)
        if sentiment_scores['pos'] > sentiment_scores['neg']:
            sentiment_labels.append('positive')
        else:
            sentiment_labels.append('negative')
    df['sentiment'] = sentiment_labels

    return df

def process_text():
    df = sentiment()
    df['reviews_text'] = df['reviews_text'].apply(lambda text: word_tokenize(text))
    df['reviews_text'] = df['reviews_text'].apply(normalize)

    return df

def export_the_dataset():
    df = process_text()
    export_path = 'ecommerce.csv'
    df.to_csv(export_path, index=False)
    return df



