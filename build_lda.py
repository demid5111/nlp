import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                     level=logging.INFO)
from gensim import corpora, models, similarities
from gensim.models.ldamodel import LdaModel

from collect_info_for_lda import collectInfo2
import shelve
NUM_TOPICS = 50

d = shelve.open('authors.list')
# result_list,authors = collectInfo()
result_list = collectInfo2()
# print result_list
d['result_list'] = result_list

dictionary = corpora.Dictionary(result_list)
dictionary.save('sample.dict')

corpus = [dictionary.doc2bow(text) for text in result_list[:]]
corpora.MmCorpus.serialize('sample.mm', corpus) # store to disk, for later use
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=NUM_TOPICS)
lda.save('hse_model.lda')

d.close()