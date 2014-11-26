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
  new_text = text
  real_authors = []
  #save real authors for the final check
  for i in new_text:
    if i in authors:
      print "Authors: ",i
      real_authors.append(i)
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
  try:
    uri2author = d['uri2author']
  except KeyError:
    print "no such key :("
  
  #visualize results - simple output to the console
  for author in author_rating:
    print "Author: " + UnicodeDammit(uri2author[author].decode('koi8-r','ignore')).unicode_markup 
    print "uri: " + author + " prob: " + str(result_dic[author])
    auth_dic[author] = result_dic[author]
    if author in real_authors:
      print "Real author found ", author_rating.index(author)+1
      try:
        author_res = d["author_res"]
      except KeyError:
        author_res = {}
        d["author_res"] = author_res
      try:
        author_res[author_rating.index(author)+1] += 1
      except KeyError:
        author_res[author_rating.index(author)+1] = 1
    if i == LIMIT_RETURN-1:
      break

    i += 1

  d.close()
  return auth_dic


def calculateCategories(text,LIMIT_RETURN=10):

  d = shelve.open('categories.list')


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
  
  #new_text = adoptText(text)
  
  doc_bow =   dictionary.doc2bow(new_text)
  # print doc_bow
  doc_lda = lda[doc_bow]
  # print doc_lda #probability that text is from the exact theme
  distribution_vec = {topicNum:probability for topicNum,probability in doc_lda}
  
  
  index = 0
  
  
  categories_distribution = {}
  bgw_per_topics =  lda.show_topics(num_topics=NUM_TOPICS,num_words=7900,formatted=False)
  
  i = 0
  for topic in bgw_per_topics:
    # info = texts[i]
    for probability,word in topic:
      word = UnicodeDammit(word).unicode_markup
      if word in categories:
        # print word
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
      except KeyError:
        continue
    if result != 0:
      result_dic[category] = result
  
  categories_rating = sorted(result_dic.keys(), key = lambda x: result_dic[x],reverse=True)
  # print author_rating
  i = 0
  categories_dic = {}
  
  
  #visualize results - simple output to the console
  for category in categories_rating:
    print "category: " + category  + " prob: " + str(result_dic[category])
    categories_dic[category] = result_dic[category]
    
    if i == LIMIT_RETURN-1:
      break
    i += 1

  d.close()
  return categories_dic


if __name__ == "__main__":

  d = shelve.open('authors.list')
  result_list = d['result_list']
  # author_res = d["author_res"]
  # author_res = {}
  base = 2166
  diff = int(len(result_list) * 0.3)
  d.close()
  print "Papers to analyze: ", diff
  for i in range (0,diff):
    print "Paper #{}".format(str(i+1))
    #calculateExperts(result_list[-i])
    calculateCategories(result_list[-i])
#   calculateExperts("""В последние годы в результате потепления климата на Крайнем Севере произошли значительные изменения. Ледяной покров Арктики исчезает очень быстрыми темпами1, а это означает повышение уровня морей, а также уменьшение жизненного пространства животных, прежде всего полярных медведей2. Тающий лед также влияет на существующую там дорожную и социальную инфраструктуру.

# С другой стороны, исчезающий арктический лед открывает перед человеком новые районы для освоения и эксплуатации (как ожидается, это вызовет рост добычи энергоресурсов и прочих полезных ископаемых), а также ведет к усилению различных форм экономической деятельности, в том числе к развитию туризма. Открытие новых судоходных путей и более тонкий ледяной покров также могут повлиять на развитие межконтинентального морского транспорта при условии создания нужной инфраструктуры.
# Для решения проблем дальнейшего развития Арктики северными странами было создано несколько региональных международных организаций, в частности Северное сотрудничество (Official co-operation in the Nordic region), которое является одной из наиболее известных и широких форм региональных контактов с участием Дании, Финляндии, Исландии, Норвегии, Швеции и трех независимых регионов: Фарерских островов, Гренландии и Аландских островов.
# Сотрудничество северных стран имеет долголетнюю традицию (с 1952 г.)5, и факторами, которые способствуют его развитию, являются: географическое положение, этническое, культурное, религиозное и частично политическое содружество. Оно охватывает много сторон социальных, экономических, культурных и политических отношений, а его участниками являются: правительство, парламенты, государственные учреждения, регионы и отдельные города.
# Региональная политика в Северном сотрудничестве от начала его формирования состояла в сглаживании различий между государствами, вытекающих из несхожей географической среды, неблагоприятного климата и небольшого населения. В настоящее время оно охватывает свыше 25 млн жителей и площадь в 3,5 млн кв. км6. Важнейшими организациями по сотрудничеству и интеграции северных государств являются Северный Совет (СС) и Совет министров Северных стран (СМСС).
# Последний был создан в 1971 г. и является межправительственным органом пяти северных стран — Дании, Исландии, Норвегии, Финляндии и Швеции, входящих в Северное сотрудничество. Имеет собственный бюджет, что позволяет ему оперативно решать вопросы, связанные с развитием Арктики. С 1997 года на основании Меморандума о взаимопонимании между Правительством РФ и СМСС в Санкт-Петербурге начало работу Информационное бюро СМСС, которое организует сотрудничество северных стран с северными регионами России в первую очередь в области образовательных и информационных программ.
# С начала 90-х годов XX века деятельность СС и СМСС в сфере международных контактов сосредоточивалась на трех главных направлениях: внутреннем сотрудничестве между северными странами; общеевропейском сотрудничестве, в частности с ЕС и с Европейской экономическим пространством; со смежными регионами Арктики и Балтийского моря, а также с Северо-Западной Россией7. Платформой для активных действий в данных географических регионах является принятая СМСС в 1990 году программа их развития «The Adjacent Areas Programme», которая считается приоритетной программой в сфере реализации внешней политики северных государств.
# В 2011 году СМСС возглавляла Финляндия. Основной темой ее председательства являлось изменения климата (особенно в Арктике), а также связанные с этим вызовы8. В Финляндии Северное сотрудничество очень ценится и пользуется, так же как и в остальных скандинавских странах, сильной общественной поддержкой. В значительной степени оно является образцом для других регионов Европы. В 2012 г. в СМСС председательствует Норвегия. Ее задачей в период председательства является повышение эффективности социальной модели государства благосостояния в северных странах в современных условиях.
# Активность северных государств в Арктике заметна и на парламентском уровне. Парламентеры обсуждают вопросы Крайнего Севера в рамках Северного Совета, а также посредством Постоянного Комитета Парламентариев Арктического Региона (SCPAR)9.
# В целом, анализируя деятельность северных стран в Арктике, необходимо отметить, что она несомненно пролила свет на социальные условия жизни в этом регионе, обратила внимание на потребность в устойчивом развитии экономики северных регионов (северные страны, в частности, поддерживают оленеводство10), а также расширила знания по проблемам загрязнения окружающей среды и климатических изменений на Крайнем Севере. (Одним из примеров является инициатива ARKUFO. В конце 2005 г. Северный Совет выразил желание исследовать изменения климата и их последствия для населения, живущего на арктических территориях. Это задание было передано NordForsk СМСС в феврале 2007 г.). Это удалось благодаря многочисленным исследованиям и докладам, финансируемым СМСС. В частности, в 2010 г. СМСС опубликовал результаты исследований, проводимых рабочей группой из стран-участниц, в отчете под заглавием «Arctic Social Indicators»12. Этот документ являлся продолжением доклада «Arctic Human Development Report» за 2004 г. («Доклад об Общественном Развитии Арктики» был первой комплексной оценкой состояния благополучия людей, живущих во всем арктическом регионе. Он представлял собой главную цель представительства Исландии в Арктическом Совете). В документе представлено несколько социальных показателей, которые отражают ключевые аспекты общественного развития в Арктике, а в будущем облегчат их наблюдение и мониторинг. Здесь речь идет, в частности, об изменениях, связанных со статусом Арктики, развитием прав коренного и местного населения и ростом экономики региона.
# Северные страны стремятся к охране чувствительных экосистем, а также к сбалансированному использованию ресурсов региона и к охране его биологического разнообразия12. Они стремятся активно участвовать в решении проблем климатических изменений, в том числе в сфере предотвращения и смягчения отрицательных последствий, вызванных потеплением климата в Арктике, при сотрудничестве в данной области с другими заинтересованными сторонами13. В связи с данной задачей СМСС обязался предпринимать усилия в пользу ограничения эмиссии тепличных газов и вредных для окружающей среды веществ, а также предоставления информации на тему существующих угроз. В 2008 году министры по охране окружающей среды северных стран приняли Северную стратегию по вопросам климата и загрязнений среды в Арктике (Nordic strategy for the Arctic climate and environmental pollutants), которая дополняет «Arctic Cooperation Programme», и «Nordic Environmental Action Plan» и является основой дальнейшего сотрудничества в рамках СМСС. В документе намечены цели и приоритеты, которые представляют собой основу для реализации конкретных экологических и других проектов в Арктике.
# СМСС также предпринимает усилия для повышения качества жизни коренного населения на арктических территориях. В рамках Международного Полярного Года (2007–2009) он финансировал проект «Survey of Living Conditions in the Arctic» (SLiCA) — «Исследование условий жизни в Арктике». Его результаты были представлены 11 мая 2011 года в Университете в Гренландии, в рамках цикла лекций, предшествующих очередной министерской встрече членов Арктического Совета в городе Нуук. В рамках проекта были определены и проанализированы условия жизни автохтонного населения в Арктике (эскимосов, саами и туземных народов Чукотки). Это было первое исследование такого типа. В нем приняли участие представители местного населения и ученые из США, Канады, Гренландии, Норвегии, Швеции, Финляндии, а также коренные жители Кольского полуострова и Чукотки в России. Исследование, которое продолжалось 10 лет, показало, что крепкие семейные связи, сеть социальной поддержки, возможность продолжать традиционные формы экономической деятельности являются главными причинами того положения дел, что большинство коренного населения довольно своей жизнью в Арктике14.
# Внимания заслуживают также меры, предпринимаемые в пользу сокращения барьеров в образовании жителей Крайнего Севера. Это происходит путем финансовой поддержки СМСС деятельности Арктического университета, который развивает образовательные связи между северными странами и поэтому с этим является эффективным инструментом улучшения качества человеческого капитала. Его слушатели приобретают знания о том, какие инструменты нужны для сохранения устойчивого развития Арктики при одновременном улучшении охраны окружающей среды. Данный Университет имеет также целью создание общей региональной структуры образования путем продвижения культурного и языкового разнообразия, поддерживает также равенство полов и одновременно обращает внимание на значение партнерства между коренным населением региона и остальными жителями Крайнего Севера.

# Сотрудничество между северными странами, направленное на то, чтобы справиться с общими вызовами, является важным аспектом их вовлечения в дела Арктики. Важнейшим из них является безопасность. «Северный Атлантический океан представляет собой важную часть Скандинавии, и у нас есть общая ответственность за безопасность в этом регионе. Это естественная область сотрудничества на северном уровне, не вспоминая уже о наших соседях <...> Новые вызовы и шансы на Северном Атлантическом океане увеличат потребность в более близком региональном и международном сотрудничестве», — такими словами председатель Северного Совета Х. Д. Кристенсен открыл конференцию на тему безопасности на море в города Торхсван (Фарерские острова) 9 июня 2011 года.
# Потепление климата дает возможность развития международного морского судоходства в арктических районах и позволит плавать по кратчайшим путям из Европы в Азию. Вместе с тем Арктика особенно восприимчива к угрозам, а небольшая плотность населения и слабо развитая инфраструктура являются причиной того, что управление этим регионом в кризисных ситуациях здесь особенно трудно. В связи с этим, безопасность Крайнего Севера требует внедрения интегрированной системы управления безопасностью морского транспорта, развития инфраструктуры, а также эффективных способов реагирования в случае аварии или катастрофы на море. Таким образом, Арктика получает новое значение в масштабе и международной экологической безопасности.
# Арктика, по нашему мнению, является новым регионом в глобальной политике (новые отношения, появляющиеся между Арктикой и внешним миром, важны с политической точки зрения — ибо они становятся существенным элементом мировой геополитики). Здесь сталкиваются интересы великих держав, в том числе и России. Параллельно с глобализацией, которая вводит в Арктику новые субъекты, международное сотрудничество в северном регионе становится все более интенсивным. На глазах международной общественности появляется интенсивно развивающийся регион весомого политического и экономического значения, что отражает новую важную тенденцию в международных отношениях.""")



