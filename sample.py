 # -*- coding: latin-1 -*-
###############################
##Author: Demidovskij A.
##Created: 19:00 15.08.14
##Last modified: 22:15 12.09.14
###############################

import sys
import operator

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                     level=logging.INFO)
from gensim import corpora, models, similarities
from gensim.models.ldamodel import LdaModel
import pymorphy2
import re
import os
import codecs
from bs4 import UnicodeDammit
import operator
# from collect_info_for_lda import collectInfo
import shelve
NUM_TOPICS = 20

# function adoptText(text)
# text - arbitrary text
# returns the split into the list text with eliminated common words
def adoptText(text):
  words = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b",
               "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
               "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                "а","б","в","г","д","е", "ё","ж","з","и","л","м","н","о",
                "п","р","с","т","у","ф","х","ц","ш","щ","ъ","ь","э","ю","я",
                "большой", "бы", "быть", "в", "весь", "вот", "все",
                "всей", "вы", "говорить", "год", "да", "для", "до", "еще",
                "же", "знать", "и", "из", "к", "как", "который", "мочь",
                "мы", "на", "наш", "не", "него", "нее", "нет", "них", "но",
                "о", "один", "она", "они", "оно", "оный", "от", "ото", "по",
                "с", "свой", "себя", "сказать", "та", "такой", "только", "тот",
                "ты", "у", "что", "это", "этот", "я", "без", "более", "больше",
                "будет", "будто", "бы", "был", "была", "были", "было", "быть",
                "вам", "вас", "ведь", "весь", "вдоль", "вдруг", "вместо",
                "вне", "вниз", "внизу", "внутри", "во", "вокруг", "вот",
                "впрочем", "все", "всегда", "всего", "всех", "всю", "вы",
                "где", "да", "давай", "давать", "даже", "для", "до",
                "достаточно", "другой", "его", "ему", "ее", "её", "ей", "если",
                "есть", "ещё", "еще", "же", "за", "за исключением", "здесь",
                "из", "из-за", "из", "или", "им", "иметь", "иногда", "их",
                "как-то", "кто", "когда", "кроме", "кто", "куда", "ли", "либо",
                "между", "меня", "мне", "много", "может", "мое", "моё", "мои",
                "мой", "мы", "на", "навсегда", "над", "надо", "наконец", "нас",
                "наш", "не", "него", "неё", "нее", "ней", "нет", "ни",
                "нибудь", "никогда", "ним", "них", "ничего", "но", "ну", "об",
                "однако", "он", "она", "они", "оно", "опять", "от", "отчего",
                "очень", "перед", "по", "под", "после", "потом", "потому",
                "потому что", "почти", "при", "про", "раз", "разве", "свою",
                "себя", "сказать", "снова","с", "со", "совсем", "так", "также",
                "такие", "такой", "там", "те", "тебя", "тем", "теперь",
                "то", "тогда", "того", "тоже", "той", "только", "том", "тот",
                "тут", "ты", "уже", "хоть", "хотя", "чего", "чего-то", "чей",
                "чем", "через", "что", "что-то", "чтоб", "чтобы", "чуть",
                "чьё", "чья", "эта", "эти", "это", "эту", "этого", "этом",
                "этот","к"]
  morph = pymorphy2.MorphAnalyzer()
  stop_string = ":.-()!,[]'\"|"
  res_list = []
  for x in text.split():
    if x not in words:
      x = x.strip(stop_string).lower()
      res_list.append(morph.parse(UnicodeDammit(x)\
                                  .unicode_markup)[0].normal_form)
  return res_list

# function calculateExperts(text)
# text - arbitrary text
# returns the dictionary of LIMIT_RETURN experts
# {expert_name:expert_probability}
# built by the LDA model
def calculateExperts(text,LIMIT_RETURN=10):

  d = shelve.open('authors.list')


  try:
    authors = d['authors']
    result_list = d['result_list']
  except KeyError:
    print "no such key :("
    # result_list,authors = collectInfo()
    # d['authors'] = authors
    # d['result_list'] = result_list

  if 'sample.dict' in os.listdir('.'):
    dictionary = corpora.Dictionary.load('sample.dict')
  else:
    print "no sample dic :("
    # dictionary = corpora.Dictionary(result_list)
    # dictionary.save('sample.dict') # store the dictionary, for future reference

  

  if 'hse_model.lda' in os.listdir('.'):
    lda = models.LdaModel.load('hse_model.lda')
  else:
    print "no hse_model.lda :("
    # corpus = [dictionary.doc2bow(text) for text in result_list[:-1]]
    # corpora.MmCorpus.serialize('sample.mm', corpus) # store to disk, for later use
    # tfidf = models.TfidfModel(corpus)
    # corpus_tfidf = tfidf[corpus]
    # lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=NUM_TOPICS)
    # lda.save('hse_model.lda')

  # lda.print_topics(20) #shows words and probability of the word in theme
  # lda = LdaModel(corpus, num_topics=NUM_TOPICS, alpha='auto', eval_every=5)
  
  #TODO: comment the line below and the line with adoptText comment out
  new_text = result_list[-1]
  # new_text = adoptText(text)
  
  doc_bow =   dictionary.doc2bow(new_text)
  # print doc_bow
  doc_lda = lda[doc_bow]
  # print doc_lda #probability that text is from the exact theme
  distribution_vec = {topicNum:probability for topicNum,probability in doc_lda}
  
  
  index = 0
  signal_w_distribution = {}
  author_num = 0
  experts_distribution = {}
  bgw_per_topics =  lda.show_topics(num_topics=NUM_TOPICS,num_words=7900,formatted=False)
  
  i = 0
  for topic in bgw_per_topics:
    # info = texts[i]
    for probability,word in topic:
      word = UnicodeDammit(word).unicode_markup
      if word in authors:
        # print word
        if i not in experts_distribution.keys():
          experts_distribution[i] = {}
        if word not in experts_distribution[i].keys():
          experts_distribution[i][word] = probability
        
        # print " ".join(["topic #",str(i),"word",word,str(probability)])
    i += 1
  #created the dictionary:
  # experts[num_topic][expert] = probability
  result_dic = {}

  for author in authors:
    result = 0
    for topic in distribution_vec:
      
      try:
        result += (experts_distribution[topic][author]   #expert for the given topic
                              * distribution_vec[topic]) #text is from the topic
      except KeyError:
        continue
    if result != 0:
      result_dic[author] = result
  author_rating = sorted(result_dic.keys(), key = lambda x: result_dic[x],reverse=True)
  # print author_rating
  i = 0
  auth_dic = {}
  for author in author_rating:
    print "Author: " + author + " prob: " + str(result_dic[author])
    auth_dic[author] = result_dic[author]
    if i == LIMIT_RETURN:
      break
    i += 1

  d.close()
  return auth_dic

if __name__ == "__main__":
  calculateExperts("text")



