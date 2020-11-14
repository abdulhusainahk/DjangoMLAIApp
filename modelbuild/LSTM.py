import gensim
model=gensim.models.KeyedVectors.load('wordvector')

sentence1='What is my name ?'
sentence2='My name is Jane Doe.'
sent1,sent2=[],[]
for i in sentence1.split():
	if i in model:
		sent1.append(model[i])
for i in sentence2.split():
	if i in model:
		sent2.append(model[i])

