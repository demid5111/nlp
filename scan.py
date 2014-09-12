from bs4 import BeautifulSoup
from nlp_models import session, HseArticle, HseAuthor
import urllib2
import re
print "Hello,world!"
##Request from DB all hse_articles
pub_dic = {}
print "Get info from db. . . "
article =  session.query(HseArticle).all()
#with open("publications","w") as  f:
for i in article:
	if i not in pub_dic.keys():
		pub_dic[i.uri] = i.id
		#f.write(i.uri+",")

# pub_list = []
# with open("publications","r") as  f:
# 	s = f.readlines()
# 	print len(s)
# 	for j in s:
# 		pub_list.extend(x for x in j.split(",") if x != "")
# #print pub_list

author2paper = {}
isEn = re.compile(".*[a-zA-Z].*")
j = 1
for pub in pub_dic.keys():
	print str(j) + " Scanning {}. . . ".format(pub)
	j += 1
	try:
		soup = BeautifulSoup(urllib2.urlopen(pub.encode('utf-8')))
	except urllib2.HTTPError as e:
		print "Page {} returns {}".format(pub.encode('utf-8'),e.code)
		continue
	tag =  soup.p

	authors =  tag.text.encode('utf-8').split(', ')
	# print authors
	for i in authors:
		if i not in author2paper.keys():
			# print i
			if isEn.match(i):
				print "ENGLISH " + i
				continue
			author2paper[i] = []
		author2paper[i].append(pub)

authors = []

for author in author2paper.keys():
	
	print "Author: " + author
	print "His papers: "
	for pub in author2paper[author]:
		tmp = HseAuthor(author_name = author,
						article_id = pub_dic[pub])
		authors.append(tmp)
		print "\t" + pub
session.add_all(authors)
session.commit()
# print soup.title.string.encode('utf-8')
# 
# print tag["class"]
# authors =  tag.text.encode('utf-8').split(', ')
# for i in authors:
# 	print i

