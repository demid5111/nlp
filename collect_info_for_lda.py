 # -*- coding: latin-1 -*-
from bs4 import BeautifulSoup
from nlp_models import session, HseArticle, HseAuthor
from sqlalchemy import distinct
import codecs
import re
import pymorphy2
from bs4 import UnicodeDammit
def collectInfo ():
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
	titles = session.query(distinct(HseArticle.title)).all()
	print "len of distinct(titles) : " + str(len(titles))
	titles_list = [x[0] for x in titles]
	# for x in titles:
	# 	print type(x[0])
		#print codecs.encode(x[0],'koi8_r')
		#print codecs.encode(x[0].decode('latin_1').encode('utf-8'),'koi8_r')
	results = session.query(HseArticle.id, HseArticle.interest,HseArticle.elib,\
							HseArticle.keyword, HseArticle.title,\
							HseArticle.abstr)\
					.filter(HseArticle.title.in_(titles_list))\
					.all()
	print "len of distinct articles(by title) : " + str(len(results))

	titles_dic = {}
	isAuthor = re.compile('^Author:\s*', re.IGNORECASE)
	isPubList = False
	isPub = re.compile('^\thttp://publications.hse.ru/view/.*', re.IGNORECASE)
	fileArr = open("logfile.txt","r").readlines()
	author_name = ""
	for line in fileArr:
		if isAuthor.match(line):
			lineArr = line.split(":")[-1].split()
			#print lineArr
			
			for l in lineArr:
				if len(l) > 3:
					print l.lower()
					author_name = l.lower()
					break
			if author_name == "":
				isPubList = False
				continue
			else:
				isPubList = True
		elif isPubList:
			if isPub.match(line):
				print line.strip() + ' ' + author_name
				pub = line.strip()
				if author_name != "":
					if pub not in titles_dic.keys():
						titles_dic[pub] = []
					if author_name not in titles_dic[pub]:
						titles_dic[pub].append(UnicodeDammit(author_name).unicode_markup)
				
	result_list = []
	authors = []
	for uri in titles_dic.keys():
		#print uri
		collected_info = []
		artice = session.query(HseArticle)\
												.filter(HseArticle.uri == uri)\
												.first()
		stop_string = ":.-()!,[]'\"|"
		abstr_list = []
		for x in artice.abstr.split():
			if x not in words:
				x = x.strip(stop_string).lower()
				abstr_list.append(morph.parse(UnicodeDammit(x).unicode_markup)[0].normal_form)


		
		keyword_list = []
		for x in artice.keyword.split(";"):
			for y in x.split(" "):
				if y not in words:
					y = y.strip(stop_string).lower()
					keyword_list.append(morph.parse(UnicodeDammit(y).unicode_markup)[0].normal_form)

		title_list = []
		for x in artice.title.split():
			if x not in words:
				x = x.strip(stop_string).lower()
				title_list.append(morph.parse(UnicodeDammit(x).unicode_markup)[0].normal_form)

		elib_list = []
		for x in artice.elib.split():
			if x not in words:
				x = x.strip(stop_string).lower()
				elib_list.append(morph.parse(UnicodeDammit(x).unicode_markup)[0].normal_form)

		interest_list = []
		for x in artice.interest.split():
			if x not in words:
				x = x.strip(stop_string).lower()
				interest_list.append(morph.parse(UnicodeDammit(x).unicode_markup)[0].normal_form)

		author_list = []
		author_list.extend(titles_dic[uri])	

		collected_info.extend(abstr_list)
		collected_info.extend(keyword_list)
		collected_info.extend(title_list)
		collected_info.extend(elib_list)
		collected_info.extend(interest_list)
		collected_info.extend(author_list)

		authors.extend(author_list)
		result_list.append(collected_info)
	return result_list,authors
	#print author_list
# print len(articles)

if __name__=="__main__":
	collectInfo()