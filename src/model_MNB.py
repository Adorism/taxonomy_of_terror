import pandas as pd
import numpy as np

from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline

vectorizer = CountVectorizer(tokenizer=tokenizeText, ngram_range=(1,1))
clf = MultinomialNB()


class MultinomialNB():
    def __init__(self, df, mode):

    
    def printNMostInformative(vectorizer, clf, N):
    
    #tried to re-do, need to fix again
    feature_names = vectorizer.get_feature_names()
    feature_with_fns = sorted(zip(clf.feature_log_prob_[0], feature_names))
    topClass1 = coefs_with_fns[:N]
    topClass2 = coefs_with_fns[:-(N + 1):-1]
    topClass3 = coefs_with_fns[:-(N + 2):-1]

    print("Class 1 best: ")
    for feat in topClass1:
        print(feat)
    
    print("Class 2 best: ")
    for feat in topClass2:
        print(feat)
    
    print( "Class 3 best: ")
    for feat in topClass3:
        print(feat)

    def pipeThrough(self):
        # a first priority to tighten up this part of code
        pipe = Pipeline([('cleanText', CleanTextTransformer()), ('vectorizer', vectorizer), ('clf', clf)])
        # data
        train1 = train['text'].tolist()
        labelsTrain1 = train['author'].tolist()
        test1 = test['text'].tolist()
        labelsTest1 = test['author'].tolist()
        # train
        pipe.fit(train1, labelsTrain1)
        # test
        preds = pipe.predict(test1)

        print("accuracy:", accuracy_score(labelsTest1, preds))
        print("Top 20 features used to predict: ")

        printNMostInformative(vectorizer, clf, 20)
        
        pipe = Pipeline([('cleanText', CleanTextTransformer()), ('vectorizer', vectorizer)])
        transform = pipe.fit_transform(train1, labelsTrain1)
        vocab = vectorizer.get_feature_names()
        
        for i in range(len(train1)):
            s = ""
        
        indexIntoVocab = transform.indices[transform.indptr[i]:transform.indptr[i+1]]
        numOccurences = transform.data[transform.indptr[i]:transform.indptr[i+1]]
        for idx, num in zip(indexIntoVocab, numOccurences):
            s += str((vocab[idx], num))

    def metric_tab (self):
        print(metrics.classification_report(labelsTest1, preds, 
                                    target_names=df['author'].unique()))

if name == '__main__':
return metrics.classification_report(labelsTest1, preds, target_names=df['author'].unique()))
