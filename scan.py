# -*- coding: koi8-r -*-
from nlp_models import session, HseArticle
import urllib2
import lxml.html
import re
from bs4 import UnicodeDammit
import shelve
##Request from DB all hse_articles
pub_dic = {}
article =  session.query(HseArticle).all()
for i in article:
	if i not in pub_dic.keys():
		pub_dic[i.uri] = i.id

author2paper = {}
author2uri = {}
isEn = re.compile(".*[a-zA-Z].*")

l = set([])
with open('publications.txt','r') as f:
	for url in f.readlines():
		l.add(url)
print len(l)
j = 1
for pub in l:
	pub = pub.decode('utf-8','ignore').rstrip()
	print str(j) + " Scanning {}. . . ".format(pub)
	
	try:
		content = urllib2.urlopen(pub.encode('utf-8')).read().decode('utf-8','ignore')
		doc = lxml.html.document_fromstring(content)
		
	except urllib2.HTTPError as e:
		print "Page {} returns {}".format(pub.encode('utf-8'),e.code)
		continue
	
	authors = doc.cssselect('p.details-authors a')
	
	for i in authors:
		author = i.text.encode('koi8-r','ignore')
		if isEn.match(author):
			print "ENGLISH " + author
			continue
		if author not in author2uri.keys():
			author2uri[author] = i.get('href')
		if author not in author2paper.keys():
			# print author
			# print i.get('href')
			
			author2paper[author] = []
		author2paper[author].append(pub)
	j += 1
	# if j == 8:
	# 	break
authors = []

uri2author = {x:y for (y,x) in author2uri.items()}
# print uri2author
d = shelve.open('authors.list')

d['author2uri'] = author2uri
d['uri2author'] = uri2author
d['authorUri2paper'] = author2paper

for author in author2paper.keys():
	
	print "Author: " + author + " Uri: " + author2uri[author]
	print "His papers: "
	for pub in author2paper[author]:
		print "\t" + pub.decode('utf-8','ignore').rstrip()



# session.add_all(authors)
# session.commit()
# print soup.title.string.encode('utf-8')
# 
# print tag["class"]
# authors =  tag.text.encode('utf-8').split(', ')
# for i in authors:
# 	print i

print "author2uri :"+ len(d['author2uri'])
print "uri2author :"+ len(d['uri2author'])

d.close()