from os import remove
from unidecode import unidecode
from nltk.tokenize import word_tokenize
import re, string, nltk, emoji

stop_words = nltk.corpus.stopwords.words('portuguese')

def translate_emoji(txt: str):
    return emoji.demojize(txt, language='pt')

def to_lower(txt: str):
    return txt.lower()

def remove_mention(txt: str):
    return re.sub(r'@[A-Za-z0-9_]+', ' ', txt)

def remove_hashtag(txt: str):
    return re.sub(r'#[A-Za-z0-9_]+', ' ', txt)

def remove_punctuation(txt: str):
    txt_ = txt
    for c in txt_:
        if c in string.punctuation:
            txt_ = txt_.replace(c, ' ')
    return txt_

def remove_link(txt: str):
    txt_ = re.sub(r'http\S+', '', txt)
    txt_ = re.sub(r'bit.ly/\S+', '', txt_)
    txt_ = txt_.strip('[link]')
    txt_ = re.sub(r'pic.twitter\S+', '', txt_)
    return txt_

def remove_av(txt: str):
    txt_ = re.sub(r'video:', '', txt)
    txt_ = re.sub(r'audio:', '', txt_)
    return txt_

def full_processing_pipeline(txt: str):
    txt_ = translate_emoji(txt)
    txt_ = to_lower(txt_)
    txt_ = remove_mention(txt_)
    txt_ = remove_hashtag(txt_)
    txt_ = remove_av(txt_)
    txt_ = remove_link(txt_)
    txt_ = remove_punctuation(txt_)
    txt_ = re.sub(r'[\d]', ' ', txt_)
    txt_ = ' '.join([word for word in word_tokenize(txt_) if len(word)>1 and word not in stop_words])
    return unidecode(txt_)

def keep_hashtags_pipeline(txt: str):
    txt_ = translate_emoji(txt)
    txt_ = to_lower(txt_)
    txt_ = remove_mention(txt_)
    txt_ = remove_av(txt_)
    txt_ = remove_link(txt_)
    txt_ = remove_punctuation(txt_)
    txt_ = re.sub(r'[\d]', ' ', txt_)
    txt_ = ' '.join([word for word in word_tokenize(txt_) if len(word)>1 and word not in stop_words])
    return unidecode(txt_)

def no_emoji_pipeline(txt: str):
    txt_ = to_lower(txt)
    txt_ = remove_mention(txt_)
    txt_ = remove_hashtag(txt_)
    txt_ = remove_av(txt_)
    txt_ = remove_link(txt_)
    txt_ = remove_punctuation(txt_)
    txt_ = re.sub(r'[\d]', ' ', txt_)
    txt_ = ' '.join([word for word in word_tokenize(txt_) if len(word)>1 and word not in stop_words])
    return unidecode(txt_)

def return_tokens(txt: str):
    return word_tokenize(txt)
    