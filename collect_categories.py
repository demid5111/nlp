from nlp_models import session,HseArticle
import re
from bs4 import UnicodeDammit
import shelve
import pymorphy2
from collect_info_for_lda import collectInfo
import codecs
morph = pymorphy2.MorphAnalyzer()

# collectInfo()
d = shelve.open('authors.list')

results = session.query(HseArticle).all();
total_categories = set([])

for article in results:
 
  if article.elib != "":
    elib = re.split(';|\s|,|\)|\(|"',article.elib)
    for i in elib:
      if i != '':
        total_categories.add(morph.parse(UnicodeDammit(i.lower()).unicode_markup)[0].normal_form)

  if article.interest != "":
    interests = re.split(';|\s|,|\)|\(|"',article.interest)
    for i in interests:
      if i != '':
        total_categories.add(morph.parse(UnicodeDammit(i.lower()).unicode_markup)[0].normal_form)

  if article.keyword != "":
    keywords = re.split(';|\s|,|\)|\(|"',article.keyword)
    for i in keywords:
        if i != '':
          total_categories.append(morph.parse(UnicodeDammit(i.lower()).unicode_markup)[0].normal_form)
        
for i in total_categories:
  print UnicodeDammit(i.decode('koi8-r','ignore')).unicode_markup 



d['categories'] = total_categories
d.close()

