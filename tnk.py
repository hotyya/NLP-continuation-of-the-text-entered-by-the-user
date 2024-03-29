import text_preprocessing as tp
import word2vec as w2v

# -*- coding: cp1251 -*-
# utf_8_sig

#tp.n_gramm(tp.text_pre())
w2v.words_to_vector(tp.text_pre())

#когда слова будешь выбирать с помощью регрессии обязательно проверяй, чтобы они не были одинаковыми