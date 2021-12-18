from textblob import TextBlob


def get_polarity(message):
    '''
    get_polarity
    returns the polarity of the input message

    '''
    return TextBlob(message).sentiment.polarity


def get_analysis(score):
    '''
    get_analysis
    returns the sentiment based on the input score
    '''
    sentiment = 'Positive'
    if score < 0:
        sentiment = 'Negative'
    elif score == 0:
        sentiment = 'Neutral'
    
    return sentiment

