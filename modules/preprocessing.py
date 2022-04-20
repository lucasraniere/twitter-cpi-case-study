from os import remove
from unidecode import unidecode
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re, string, nltk, emoji, spacy

nlp = spacy.load('pt_core_news_sm')
stop_words = nltk.corpus.stopwords.words('portuguese')

def remove_emoji(tweet):
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

def remove_stopwords(txt: str):
    txt_tokens = txt.split()
    new_txt = [token for token in txt_tokens if token not in stop_words and len(token)>2]
    return ' '.join(new_txt)

def lemmatizer(txt: str, **kwargs):
    lib = kwargs.get('lib')
    if lib == 'spacy':
        new_txt = [token.lemma_ for token in nlp(txt)]
    elif lib == 'nltk':
        lemm = WordNetLemmatizer()
        new_txt = [lemm.lemmatize(token) for token in txt.split()]
    else:
        new_txt = [token for token in txt.split()]
    return ' '.join(new_txt)

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