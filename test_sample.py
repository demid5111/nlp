 # -*- coding: utf-8 -*-
###############################
##Author: Demidovskij A.
##Created: 19:00 15.08.14
##Last modified: 22:15 12.09.14
###############################
import logging
#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
  #                   level=logging.INFO)
from gensim import corpora, models, similarities
from gensim.models.ldamodel import LdaModel
import pymorphy2
import sys
import os
#from bs4 import UnicodeDammit
import shelve, pickle


NUM_TOPICS = 25

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
  words = [word.decode('utf-8') for word in words]
  morph = pymorphy2.MorphAnalyzer()
  stop_string = ":.-()!,[]'\"|"
  res_list = []
  for x in text.split():
    #x = UnicodeDammit(x).unicode_markup
    x = x.decode('utf-8')
    x = x.strip(stop_string).lower()
    if x not in words:
      
      res_list.append(morph.parse(x)[0].normal_form)
  #/#print len(text)
  #/#print len(" ".join(res_list))
  return res_list

# function calculateExperts(text)
# text - arbitrary text
# returns the dictionary of LIMIT_RETURN experts
# {expert_name:expert_probability}
# built by the LDA model
def calculateExperts(text,LIMIT_RETURN=10):
  #temp = sys.stdout 
  #sys.stdout = open('log.txt', 'a')

  d = shelve.open('/home/nick/public_html/test.sapienta.ru/public/cgi-glob/nlp/authors.list')
  d1={}
  with open('/home/nick/public_html/test.sapienta.ru/public/cgi-glob/nlp/dict.pickle', 'rb') as f1:
    d1 = pickle.load(f1)
  d2={}
  for key1 in d1:
    key2=key1.encode('utf-8').replace('\r','')
    d2[key2]=d1[key1]

  try:
    uri2author = d['uri2author']
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

  # res_size = len(result_list)
  # print res_size
  # res_base = res_size
  # print res_base

  #load lda model from the shelve dictionary
  if 'hse_model.lda' in os.listdir('.'):
    lda = models.LdaModel.load('hse_model.lda')
  else:
    print "no hse_model.lda :("
    # corpus = [dictionary.doc2bow(text) for text in result_list[:]]
    # corpora.MmCorpus.serialize('sample.mm', corpus) # store to disk, for later use
    # tfidf = models.TfidfModel(corpus)
    # corpus_tfidf = tfidf[corpus]
    # lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=NUM_TOPICS)
    # lda.save('hse_model.lda')

  # lda.print_topics(20) #shows words and probability of the word in theme
  # lda = LdaModel(corpus, num_topics=NUM_TOPICS, alpha='auto', eval_every=5)
  
  #TODO: comment the line below and the line with adoptText comment out
  # new_text = result_list[-2]
  #/#lda.print_topics(25)
  authors = set([])
  for i in uri2author.keys():
    authors.add(i) 
  
  new_text = text
  real_authors = []
  #save real authors for the final check
  # for i in new_text:
  #   i = UnicodeDammit(i).unicode_markup
  #   if i in authors:
  #     print "Authors: ",i
  #     real_authors.append(i)
  new_text = adoptText(text)
  
  doc_bow =   dictionary.doc2bow(new_text)
  #print doc_bow
  doc_lda = lda[doc_bow]
  # print doc_lda #probability that text is from the exact theme
  distribution_vec={}
  for topicNum,probability in doc_lda:
    distribution_vec[topicNum]=probability
  
  index = 0
  signal_w_distribution = {}
  author_num = 0
  experts_distribution = {}
  bgw_per_topics =  lda.show_topics(num_topics=NUM_TOPICS,num_words=7900,formatted=False)
  
  i = 0
  for topic in bgw_per_topics:
    # info = texts[i]
    for probability,word in topic:
      #word = UnicodeDammit(word).unicode_markup
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
      try:
        result_dic[author] = result*100.0/d2[author]
        #print author, d2[author], result_dic[author]
      except:
        print "Error 01"
  author_rating = sorted(result_dic.keys(), key = lambda x: result_dic[x],reverse=True)

  # print author_rating
  i = 0
  auth_dic = {}
  try:
    uri2author = d['uri2author']
  except KeyError:
    print "no such key :("
  
  #visualize results - simple output to the console
  for author in author_rating:
    #print "Author: " + UnicodeDammit(uri2author[author].decode('koi8-r','ignore')).unicode_markup 
    #print uri2author[author].encode('utf-8')
    print author# + " prob: " + str(result_dic[author])
    auth_dic[author] = result_dic[author]
    # if author in real_authors:
    #   print "Real author found ", author_rating.index(author)+1
    
    if i == LIMIT_RETURN-1:
        break

    i += 1

  d.close()
  #sys.stdout.close()                # Вытолкнуть буферы на диск
  #sys.stdout = temp
  return auth_dic


def calculateCategories(text,LIMIT_RETURN=10):
  #temp = sys.stdout 
  #sys.stdout = open('log.txt', 'a')

  d = shelve.open('categories.list')
  d1={}
  with open('/home/nick/public_html/test.sapienta.ru/public/cgi-glob/nlp/dict.pickle', 'rb') as f1:
    d1 = pickle.load(f1)
  d2={}
  for key1 in d1:
    key2=key1.encode('utf-8').replace('\r','')
    d2[key2]=d1[key1]

  try:
    categories = d['categories']
  except KeyError:
    print "no such key :("
    return

  if 'sample.dict' in os.listdir('.'):
    dictionary = corpora.Dictionary.load('sample.dict')
  else:
    print "no sample dic :("
    return

  
  #load lda model from the shelve dictionary
  if 'hse_model.lda' in os.listdir('.'):
    lda = models.LdaModel.load('hse_model.lda')
  else:
    print "no hse_model.lda :("
    return

 
  
  #TODO: comment the line below and the line with adoptText comment out
  # new_text = result_list[-2]
  new_text = text
  
  new_text = adoptText(text)
  
  doc_bow =   dictionary.doc2bow(new_text)
  # print doc_bow
  doc_lda = lda[doc_bow]
  # print doc_lda #probability that text is from the exact theme
  distribution_vec={}
  for topicNum,probability in doc_lda:
    distribution_vec[topicNum]=probability
  
  
  index = 0
  
  
  categories_distribution = {}
  bgw_per_topics =  lda.show_topics(num_topics=NUM_TOPICS,num_words=10,formatted=False)
  #for i in bgw_per_topics:
  #  print i
  # print lda.show_topics(num_topics=NUM_TOPICS,num_words=7900,formatted=True)
  #print len(bgw_per_topics)
  i = 0
  for topic in bgw_per_topics:
    # info = texts[i]
    for probability,word in topic:
      #word = UnicodeDammit(word).unicode_markup
      
      if word in categories:
        
        if i not in categories_distribution.keys():
          categories_distribution[i] = {}
        if word not in categories_distribution[i].keys():
          categories_distribution[i][word] = probability
    i += 1
  #created the dictionary:
  # experts[num_topic][expert] = probability
  result_dic = {}

  for category in categories:
    result = 0
    for topic in distribution_vec:
      
      try:
        result += (categories_distribution[topic][category]   #expert for the given topic
                              * distribution_vec[topic]) #text is from the topic
        # print "Category: "
        # print category
        # print "Topic: " + str(topic)
        # print "Probability of topic: "+ str(distribution_vec[topic])
        # print "Word from a topic: "+ str(categories_distribution[topic][category])
      except KeyError:
        continue
    if result != 0:
      try:
        #print category.encode('utf-8'), d2[category.encode('utf-8')]
        result_dic[category.encode('utf-8')] = result*100.0/d2[category.encode('utf-8')]
        #print result_dic[category.encode('utf-8')]
      except:
        print "Error 02", category.encode('utf-8')

  tmp={}
  for y,x in distribution_vec.items():
    tmp[x]=y
  #/#print "Topic distribution:\n# topic \t probability"
  #/#for i in sorted(tmp,reverse=True):
  #/#  print str(tmp[i]) + "\t" + str(i)
  #/#print "\n"
  categories_rating = sorted(result_dic.keys(), key = lambda x: result_dic[x],reverse=True)
  # print author_rating
  i = 0
  categories_dic = {}
  
  
  #visualize results - simple output to the console
  for category in categories_rating:
    #print "category: " + category  + " prob: " + str(result_dic[category])
    print category#.encode('utf-8')
    categories_dic[category] = result_dic[category]
    
    if i == LIMIT_RETURN-1:
      break
    i += 1

  d.close()
  #sys.stdout.close()                # Вытолкнуть буферы на диск
  #sys.stdout = temp
  return categories_dic


if __name__ == "__main__":
  temp = sys.stdout 
  sys.stdout = open('log.txt', 'a')

  #d = shelve.open('authors.list')
  #result_list = d['result_list']
  ## author_res = d["author_res"]
  ## author_res = {}
  #base = 2166
  #diff = int(len(result_list) * 0.3)
  #d.close()
  ## print "Papers to analyze: ", diff
  ## for i in range (0,diff):
  ##   print "Paper #{}".format(str(i+1))
  
  mystr = """
КС встал на защиту кредиторов фирм-банкротов
Конституционный суд РФ (КС) признал неконституционным положение ФЗ "О госрегистрации юридических лиц", по которому компанию-банкрота могли исключить из Единого государственного реестра юридических лиц (ЕГРЮЛ). Поводом для рассмотрения дела стало обращение фирмы ООО "Отделсервис" из Алтайского края.

"""
 
  calculateExperts(mystr)
  calculateCategories(mystr)
  sys.stdout.close()                # Вытолкнуть буферы на диск
  sys.stdout = temp

