import nltk


def is_english(message,
               english_words,
               important_words):

    '''
    is_english :
    to check if the message is an english language message

    Arguments:

    message

     type: string 
     The message to be checked  

    english_words:

     type: list 
     The words allowed in english language

    important_words:

     type : list 
     The words important in the given context
    '''
    result = True
    for word in nltk.wordpunct_tokenize(message):
        if result == False:
            break
        word_validity = word.lower() in english_words or not word.isalpha() or word.upper() in important_words
        result = result and word_validity
    return result

def has_important_words(message,
                        important_words):
    '''
    has_important_words :
    to check if the message has at least one of the important words.

    Arguments:

    message

     type: string 
     The message to be checked   

    important_words:

     type : list 
     The words important in the given context
    '''
    result = False
    words_in_message = nltk.wordpunct_tokenize(message.lower())
    for word in important_words:
        if result == True:
            break
        word_validity = word.lower() in words_in_message 
        result = result or word_validity
    return result

def is_valid_date(date):
    '''
    is_valid :
    to check if the given date is in valid range of dates.

    Arguments:

    date
     type: string 
     The date to be checked
    '''
    result = False
    year, month, day = map(int, date.split('-'))
    if year == 2021 and month == 5:
        if day>=1 and day<=15:
            result = True
    return result

    
