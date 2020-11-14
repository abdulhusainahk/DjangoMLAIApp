import gensim

model=gensim.models.KeyedVectors.load_word2vec_format('E:/Final_year_project/GoogleNews-vectors-negative300.bin',binary=True,limit=50000)
model.init_sims(replace=True)
model.save('wordvector')