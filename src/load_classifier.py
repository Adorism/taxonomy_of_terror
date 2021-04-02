import pandas as pd
import numpy as np
from text_process import Corpus_prep
from model_MNB import NBmode
from model_MNB import Report




if name == '__main__':

df = pd.read_csv('../data/train.csv')
corpus_prepped = Coprus_prep(df, 'text', 'author')
model_accuracy = NBmode()
classed_report = Report()