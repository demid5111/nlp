#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import collections
import pickle

def counter(db):

    select = db.cursor()
    f = "C:\pickle.txt"
    my_file = open(f, "wb")
    i = 0
    dict = {}
    select.execute('SELECT id, interest, elib, keywords,authors FROM test1')
    list_authors = []
    list_keyword = []
    for row in select:

        field = 'authors'
        dict[field] = row[i + 4].lower().replace(',', ';')
        dict[field] = dict[field].split(';')
        for k in dict[field]:
            k = k.lstrip().rstrip()
            if k != ''.decode('utf-8'):
                list_authors.append(k)


        field = 'interest'
        dict[field] = row[i + 1].lower().replace(',', ';')
        dict[field] = dict['interest'].split(';')
        for k in dict[field]:
            k = k.lstrip().rstrip()
            if k != ''.decode('utf-8'):
                list_keyword.append(k)


        field = 'elib'
        dict[field] = row[i + 2].lower().replace(',', ';')
        dict[field] = dict[field].split(';')
        for k in dict[field]:
            k = k.lstrip().rstrip()
            if k != ''.decode('utf-8'):
                list_keyword.append(k)

        field = 'keyword'
        dict[field] = row[i + 3].lower().replace(',', ';')
        dict[field] = dict[field].split(';')
        for k in dict[field]:
            k = k.lstrip().rstrip()
            if k != ''.decode('utf-8'):
                list_keyword.append(k)

    pickle.dump(collections.Counter(list_keyword), my_file)
    pickle.dump(collections.Counter(list_authors), my_file)

    #print collections.Counter(list_keyword)
    #print collections.Counter(list_authors)
    #pickle.dump(dict(collections.Counter(list_keyword)), my_file)
    #pickle.dump(dict(collections.Counter(list_authors)), my_file)
    #my_file.write('Authors_Count:\n')
    #my_file.write(str(collections.Counter(list_authors)))
    #my_file.write('\nKeywords_Count:\n')
   # my_file.write(str(collections.Counter(list_keyword)))

    select.close()
    db.close()

db = MySQLdb.connect(host='localhost', user='root', db='test1', charset='utf8', init_command='SET NAMES UTF8')
if __name__ == '__main__':
    counter(db)