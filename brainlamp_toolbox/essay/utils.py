"""Utils essay."""
import nltk

sent_tokenizer = nltk.data.load('tokenizers/punkt/portuguese.pickle')
stopwords = nltk.corpus.stopwords.words('portuguese')


def tokenize(text):
    """Tokenize a string to split off punctuation other than periods.

    param text: tring to split
    type text: str
    return: list of string
    rtype: list
    """
    return nltk.tokenize.word_tokenize(text)


def get_sentences(text):
    """Sentence segmentation.

    param text: tring to split
    type text: str
    return: list of string
    rtype: list
    """
    return sent_tokenizer.tokenize(text)
