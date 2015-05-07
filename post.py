#!/usr/bin/python
 #-*- coding:  utf-8 -*-

import urllib
import lxml.html
import json
import MySQLdb
import threading
import os
import subprocess
import sys
import cgi
from process import process

def expert_prepare(_url):
    dictionary = {}

    db = MySQLdb.connect(host='localhost', user='root',passwd='123qwe', db='infoport', charset='utf8', init_command='SET NAMES UTF8')
    cursor = db.cursor()
    cursor.execute('select interest, article_id from exbd')
    result = cursor.fetchall()
    i = 0
    k = 0
    listkeys = []
    dictkeys = {}
    for record in result:
        if record[i+1] == _url:#!=
            dictkeys[k] = record[i]
            k=k+1
            #listkeys.append(record[i])

    dictionary['keyword'] = dictkeys
            #dictionary['keyword'] = dictkeys.get('keys')
            #dictionary['keyword'] = listkeys


    #print dictionary['keyword']


    html = urllib.urlopen(_url)
    doc = lxml.html.document_fromstring(html.read().decode('utf-8', 'ignore'))
    post = doc.cssselect('div.main .person-appointment-title')[0]
    dictionary['pos'] = post.text  #.encode('utf-8')
    academictitle = doc.cssselect('div.main .person-appointment-title')[0]
    dictionary['academic_title'] = academictitle.text  #.encode('utf-8')
    fio = doc.cssselect('div.footer__breadcrumbs .b ')[0]  #ФИО
    dictionary['fio'] = fio.text  #.encode('utf-8')
    items = doc.cssselect('div.g-pic')
    for item in items:
        image = item.get('style')
    s = image.split("'")
    page = 'http://www.hse.ru' + s[1]
    person_id = page.split("/")
    dictionary['person_id'] = person_id[6]
    #print page#адрес страницы, где находится фотография
    place = doc.cssselect('div.main .person-appointment-title + .link')
    #dictionary['place'] = place[0].text
    #print place[1].text #вывод ГОРОДА
    dictionary['photo'] = page
    #json_data = json.dumps(dictionary)
    #print json_data
    return dictionary


def json_formation(urls, _categ_list):
    dict_of_dict = '{'
    i = 0
    for url in urls:
        e_i_dict = expert_prepare(urls[i])
        e_i_dict['rkw']=_categ_list[i]
        e_i = json.dumps(e_i_dict)
        if i + 1 < len(urls):

            dict_of_dict = dict_of_dict + '"' + str(urls[i]) + '":%s,' % e_i
        else:
            dict_of_dict = dict_of_dict + '"' + str(urls[i]) + '":%s' % e_i
        i = i + 1
    dict_of_dict = dict_of_dict + '}'
    #print dict_of_dict
    return dict_of_dict

    
def main():
    #mystr = "изучением    видных советских теоретиков права, которые были приведены выше."
    print "Content-type:text/html\n"
    form = cgi.FieldStorage()
    mystr = form.getvalue('name')
    #t = threading.Thread(target = printok, args = (15,))
    #t.daemon = True
    #t.start()
    expert_list, categ_list=process(mystr)
    #print expert_list, categ_dict
    print json_formation(expert_list, categ_list)#['http://www.hse.ru/org/persons/201866', 'http://www.hse.ru/org/persons/140394']
  
if __name__ == '__main__':
    jsr = main()
