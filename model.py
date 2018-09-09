from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
import pymongo
from ml_dev import preprocess


def pull_train_data(db):
    fake_news = db.docs.aggregate([{"$limit": db.docs.count_documents({"truth": True})}, {"$match": {"truth": False}}])
    real_news = db.docs.find({"truth": True})
    
    return list(zip(real_news, fake_news))


def train_model(db):
    data = pull_train_data(db)
    X = []
    y = []

    # preprocess
    for d in data:
        X.append(preprocess.tfidf_preprocess(d['text']))
        y.append(d['truth'])
    
    pipe = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('xgb', XGBClassifier())
    ])

    pipe.fit(X, y)
    return pipe

