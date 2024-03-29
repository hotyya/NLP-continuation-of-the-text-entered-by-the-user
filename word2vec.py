from gensim.models import Word2Vec
from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression
import text_preprocessing as tp
import nltk
import pandas as pd
import numpy as np

def words_to_vector(text_):
    used_set = set()
    #orig_ = text_
    text = nltk.sent_tokenize(text_)
    text_ = [nltk.word_tokenize(sent) for sent in text]
    for i in range(len(text_)): 
        text_[i] = [w for w in text_[i] if w not in stopwords.words('english')]
    orig_ = ' '.join(text_[0])
    word2vec = Word2Vec(text_, min_count = 1)

    #for i in range(len(train_text)): 
       #train_text[i] = [w for w in train_text[i] if w not in stopwords.words('english')]
    
    train_text = [0]*len(text_[0])
    train_y = [0]*len(text_[0])

    for i in range(len(text_[0]) // 2):
        train_text[i] = list(word2vec.wv[text_[0][i]]) + list(word2vec.wv[text_[0][i + 1]]) + list(word2vec.wv[text_[0][i + 2]])
        train_y[i] = 1
        for j in range(len(text_[0]) // 2 - 1):
            if word2vec.wv.similarity(text_[0][i], text_[0][len(text_[0]) // 2 + j]) < 0.3:
                train_text[len(text_[0]) // 2 + i] = list(word2vec.wv[text_[0][i]]) + list(word2vec.wv[text_[0][len(text_[0]) // 2 + j]]) + list(word2vec.wv[text_[0][i + 2]])
                train_y[len(text_[0]) // 2 + i] = 0
                break

    train_data = pd.DataFrame(train_text)
    target_col = pd.DataFrame(train_y)

    log_reg = LogisticRegression(C = 2., solver = 'saga', penalty = 'l2')
    log_reg.fit(train_data, target_col)

    n = int(input())
    string = input()
    text = nltk.sent_tokenize(string)
    sentence = [nltk.word_tokenize(sent) for sent in text]
    dict_ = tp.n_gramm(orig_)

    for i in range(n - 1):
        pos_words = dict_[sentence[0][i + 1]]
        data_ = [0] * len(pos_words)
        for j in range(len(pos_words)):
            data_[j] = list(word2vec.wv[sentence[0][i]]) + list(word2vec.wv[sentence[0][i + 1]]) + list(word2vec.wv[pos_words[j]])
        data = pd.DataFrame(data_)
        pred_ = log_reg.predict_proba(data)[:, 1]
        k = pred_.argmax()
        while pos_words[k] in used_set:
            pred_ = np.delete(pred_, k)
            k = pred_.argmax()
        sentence[0].append(pos_words[k])
        used_set.add(pos_words[k])

    output_ = ' '.join(sentence[0])
    print(output_)
