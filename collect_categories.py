# -*- coding: utf-8 -*-

#from nlp_models import session,HseArticle
import re
#from bs4 import UnicodeDammit
import shelve
#import pymorphy2
#from collect_info_for_lda import collectInfo
#import codecs
import MySQLdb as sql
#morph = pymorphy2.MorphAnalyzer()

# collectInfo()
d = shelve.open('categories.list')

#results = session.query(HseArticle).all();
total_categories = set([])


db = sql.connect(host="localhost", user="root", passwd="newpass", db="nlp", charset='utf8')
cursor = db.cursor()
sql = """SELECT interest, elib, keyword FROM hse_article"""
cursor.execute(sql)
data =  cursor.fetchall()
#for rec in data:
#    interest1, elib1, keyword1 = rec
#    print interest1, elib1, keyword1
db.close()

for article in data:
  elib2=article[1]
  if elib2 != "":
    elib = re.split(';|,',elib2)
    for i in elib:
      if i != '':
        total_categories.add(i.lower().strip())

  interest2=article[0]
  if interest2 != "":
    interests = re.split(';|,',interest2)
    for i in interests:
      if i != '':
        total_categories.add(i.lower().strip())
  keyword2=article[2]
  if keyword2 != "":
    keywords = re.split(';|,|\)|\(|"',keyword2)
    for i in keywords:
        if i != '':
          try:
            total_categories.add(i.lower().strip())
          except:
            pass
for i in total_categories:
  print i



d['categories'] = total_categories
d.close()

