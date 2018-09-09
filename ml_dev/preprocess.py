from textblob import TextBlob
from nltk.corpus import stopwords, words


stops = set(stopwords.words())
english_words = set(w.lower() for w in words.words())


def preprocess(corpus):
    blob = TextBlob(corpus)
    ret = []
    for sent in blob.sentences:
        sent_list = []
        for word in sent.words.lower().lemmatize():
            if word in english_words and word not in stops:
                sent_list.append(word)
        ret.append(sent_list)
    return ret

def tfidf_preprocess(corpus):
    blob = TextBlob(corpus)
    ret = []
<<<<<<< HEAD
    for word in blob.words.lower():
        if word in english_words and word not in stops:
            ret.append(word)
    return ' '.join(ret)

=======
    for word in blob.words:
        if word in english_words and word not in stops:
            ret.append(word)
    return ' '.join(ret)
>>>>>>> ec2b3526ae981fcf3aeee2ff4986b36ed5143b41
