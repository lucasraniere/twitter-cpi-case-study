'''
This module contains function to text processing
focused on tweets.

The preprocessing techniques in this modules are:
    - emoji removal
    - emoji translation to portuguese
    - mentions removal
    - hashtags removal
    - punctuation removal
    - stop words removal
    - lemmatizer
    - video and audio tags removal
    - links and url removal
'''

import re
import string
from unidecode import unidecode
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import emoji
import nltk
import spacy

nlp = spacy.load('pt_core_news_sm')
stop_words = nltk.corpus.stopwords.words('portuguese')
stop_words.extend(['pra', 'tá', 'ta', 'tão', 'porque'])


def remove_emoji(tweet):
    '''
    Remove emojis from tweets.

        Parameters:
            tweet (str): textual content of a tweet

        Returns:
            (str): the textual content of the original
            tweet without emojis
    '''
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return emoji_pattern.sub(r'', tweet)


def translate_emoji(txt: str):
    '''
    Translate emojis to portuguese.

    Parameters:
        txt (str): tweet textual content

    Returns:
        (str): same tweet, but with the
        emojis replaced by the translations.
    '''
    return emoji.demojize(txt, language='pt')


def remove_mention(txt: str):
    '''
    Remove mentions from tweets
    A mention has the pattern: @NameOfUser

    Parameters:
        txt (str): tweet textual content

    Returns:
        (str): same tweet without mentions
    '''
    return re.sub(r'@[A-Za-z0-9_]+', ' ', txt)


def remove_hashtag(txt: str):
    '''
    Remove hashtags from tweets
    A hashtag has the pattern: #SomeHahstag

    Parameters:
        txt (str): tweet textual content

    Returns:
        (str): same tweet without hashtags
    '''
    return re.sub(r'#[A-Za-z0-9_]+', ' ', txt)


def remove_punctuation(txt: str):
    '''
    Remove punctuation from tweets

    Parameters:
        txt (str): tweet textual content

    Returns:
        (str): same tweet without punctuation
    '''
    txt_ = txt
    for char in txt_:
        if char in string.punctuation:
            txt_ = txt_.replace(char, ' ')
    return txt_


def remove_stopwords(txt: str):
    '''
    Remove stop words from tweets

    Parameters:
        txt (str): tweet textual content

    Returns:
        (str): same tweet without stop words
    '''
    txt_tokens = txt.split()
    new_txt = [token for token in txt_tokens if token not in stop_words and len(token) > 2]
    return ' '.join(new_txt)


def lemmatizer(txt: str, **kwargs):
    '''
    Lemmatize the tweet

    Parameters:
        txt (str): tweet textual content

    Returns:
        (str): same tweet but "lemmatized"
    '''
    lib = kwargs.get('lib')
    if lib == 'spacy':
        new_txt = [token.lemma_ for token in nlp(txt)]
    elif lib == 'nltk':
        lemm = WordNetLemmatizer()
        new_txt = [lemm.lemmatize(token) for token in txt.split()]
    else:
        new_txt = list(txt.split())
    return ' '.join(new_txt)


def remove_link(txt: str):
    '''
    Remove links and urls from tweets

    Parameters:
        txt (str): tweet textual content

    Returns:
        txt_ (str): same tweet without links and urls
    '''
    txt_ = re.sub(r'http\S+', '', txt)
    txt_ = re.sub(r'bit.ly/\S+', '', txt_)
    txt_ = txt_.strip('[link]')
    txt_ = re.sub(r'pic.twitter\S+', '', txt_)
    return txt_


def remove_av(txt: str):
    '''
    Remove audio and video tags from tweets
    A A/V tag has the pattern: VIDEO:http...

    Parameters:
        txt (str): tweet textual content

    Returns:
        txt_ (str): same tweet without audio
        and video tags
    '''
    txt_ = re.sub(r'video:', '', txt)
    txt_ = re.sub(r'audio:', '', txt_)
    return txt_


def full_processing_pipeline(txt: str):
    '''
    Run a preprocessing pipeline with all the
    preprocessing functions

    Parameters:
        txt (str): tweet textual content

    Returns:
        txt_ (str): same tweet, but with translated
        emojis, in lower case, and removing mentions,
        hashtags, A/V tags, links and urls, and
        punctuations
    '''
    txt_ = translate_emoji(txt)
    txt_ = txt_.lower()
    txt_ = remove_mention(txt_)
    txt_ = remove_hashtag(txt_)
    txt_ = remove_av(txt_)
    txt_ = remove_link(txt_)
    txt_ = remove_punctuation(txt_)
    txt_ = re.sub(r'[\d]', ' ', txt_)
    txt_ = ' '.join([word for word in word_tokenize(txt_)
    if len(word) > 1 and word not in stop_words])
    return unidecode(txt_)


def keep_hashtags_pipeline(txt: str):
    '''
    Run a preprocessing pipeline keeping the
    hashtags

    Parameters:
        txt (str): tweet textual content

    Returns:
        txt_ (str): same tweet, but with translated
        emojis, in lower case, and removing mentions,
        A/V tags, links and urls, and punctuations.
        Hahstags are not removed.
    '''
    txt_ = translate_emoji(txt)
    txt_ = txt_.lower()
    txt_ = remove_mention(txt_)
    txt_ = remove_av(txt_)
    txt_ = remove_link(txt_)
    txt_ = remove_punctuation(txt_)
    txt_ = re.sub(r'[\d]', ' ', txt_)
    txt_ = ' '.join([word for word in word_tokenize(txt_)
    if len(word) > 1 and word not in stop_words])
    return unidecode(txt_)


def no_emoji_pipeline(txt: str):
    '''
    Run a preprocessing pipeline removing the emojis

    Parameters:
        txt (str): tweet textual content

    Returns:
        txt_ (str): same tweet, but in lower case, and
        removing emojis, mentions, hashtags, A/V tags,
        links and urls, and punctuations
    '''
    txt_ = txt.lower()
    txt_ = remove_mention(txt_)
    txt_ = remove_hashtag(txt_)
    txt_ = remove_av(txt_)
    txt_ = remove_link(txt_)
    txt_ = remove_punctuation(txt_)
    txt_ = re.sub(r'[\d]', ' ', txt_)
    txt_ = ' '.join([word for word in word_tokenize(txt_)
    if len(word) > 1 and word not in stop_words])
    return unidecode(txt_)


def no_mention_no_emoji_pipeline(txt: str):
    '''
    Run a preprocessing pipeline removing emojis and
    mentions, and keeping the hastags

    Parameters:
        txt (str): tweet textual content

    Returns:
        txt_ (str): same tweet, but in lower case, and
        removing emojis, mentions, A/V tags, links and urls,
        and punctuations
    '''
    txt_ = txt.lower()
    txt_ = remove_emoji(txt_)
    txt_ = remove_mention(txt_)
    txt_ = remove_av(txt_)
    txt_ = remove_link(txt_)
    txt_ = remove_punctuation(txt_)
    txt_ = re.sub(r'[\d]', ' ', txt_)
    txt_ = ' '.join([word for word in word_tokenize(txt_)
    if len(word) > 1 and word not in stop_words])
    return unidecode(txt_)


def return_tokens(txt: str):
    '''
    Return tokens from tweets

    Parameters:
        txt (str): tweet textual content

    Returns:
        (list): textual tokens from original tweet
    '''
    return word_tokenize(txt)
