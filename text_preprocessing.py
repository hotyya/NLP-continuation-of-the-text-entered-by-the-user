import nltk
import re
import codecs

def text_pre():
    #with open("brothers.txt", "r") as file:
        #text_ = file.read()
        #text_ = text_.lower()
        #text_ = re.sub('[^a-zA-Z]', ' ', text_)
        #text_ = re.sub(r'\s+', ' ', text_)

    fileObj = codecs.open( "try.txt", "r", "cp1251" )
    text_ = fileObj.read()
    fileObj.close()
    text_ = text_.lower()
    text_ = re.sub('[^a-zA-Z]', ' ', text_)
    text_ = re.sub(r'\s+', ' ', text_)
    text_ = text_[6:]
    return text_

def n_gramm(text_):
    dict_ = dict()
    n_gramm = list(text_.split())
    for i in range(len(n_gramm)):
        if i == 0:
            dict_[n_gramm[i]] = list(set([n_gramm[i + 1], n_gramm[i + 2]]))
        elif i == 1:
            if n_gramm[i] in dict_:
                dict_[n_gramm[i]] = list(set([n_gramm[i - 1], n_gramm[i + 1], n_gramm[i + 2]]
                                        + dict_[n_gramm[i]]))
            else:
                dict_[n_gramm[i]] = list(set([n_gramm[i - 1], n_gramm[i + 1], n_gramm[i + 2]]))
        elif i == len(n_gramm) - 1:
            if n_gramm[i] in dict_:
                dict_[n_gramm[i]] = list(set([n_gramm[i - 2], n_gramm[i - 1]] 
                                     + dict_[n_gramm[i]]))
            else: 
                dict_[n_gramm[i]] = list(set([n_gramm[i - 2], n_gramm[i - 1]]))    
        elif i == len(n_gramm) - 2:
            if n_gramm[i] in dict_:
                dict_[n_gramm[i]] = list(set([n_gramm[i - 2], n_gramm[i - 1], n_gramm[i + 1]]
                                        + dict_[n_gramm[i]]))
            else:
                dict_[n_gramm[i]] = list(set([n_gramm[i - 2], n_gramm[i - 1], n_gramm[i + 1]]))
        else:
            if n_gramm[i] in dict_:
                dict_[n_gramm[i]] = list(set([n_gramm[i - 2], n_gramm[i - 1], 
                                        n_gramm[i + 1], n_gramm[i + 2]]
                                        + dict_[n_gramm[i]]))
            else:
                dict_[n_gramm[i]] = list(set([n_gramm[i - 2], n_gramm[i - 1], 
                                        n_gramm[i + 1], n_gramm[i + 2]]))

    return dict_


