#!/usr/bin/python
# -*- coding:  utf-8 -*-

# Import modules for CGI handling ;s
import urllib
import lxml.html
import string
import json

url = 'http://www.hse.ru/staff/nkarpov'
#url - любую персональную страницу сотрудника

def main():
    html = urllib.urlopen(url)
    doc = lxml.html.document_fromstring(html.read().decode('utf-8', 'ignore'))
    post = doc.cssselect('div.main .person-appointment-title')[0]
    print post.text#должность
    post1 = urllib.urlencode(post)
    #print p
    academictitle = doc.cssselect('div.main .person-appointment-title')[1]
    print academictitle.text#ученое звание
    academictitle1 = urllib.urlencode(academictitle)
    fio = doc.cssselect('div.footer__breadcrumbs .b ')[0]#ФИО
    print fio.text#ФИО
    fio1 = urllib.urlencode(fio)
    items = doc.cssselect('div.g-pic')
    for item in items:
        image = item.get('style')
        #print image
    s = image.split("'")
    #print s[1]
    page = 'hse.ru'+s[1]#адрес страницы, где находится фотография
    print page #hse.ru/pubs/share/direct/138568616
    dictionary = {'post':post1,'academic title': academictitle1, 'fio': fio1, 'photo': page}#словарь который нужно преобразовать для JSON
    print dictionary #print dictionary {'academic title': 'class=person-appointment-title', 'post': 'class=person-appointment-title', 'fio': 'class=b', 'photo': 'hse.ru/pubs/share/direct/138568616'}
    #print(json.dumps((d),sort_keys=True))
    json_data = json.dumps(dictionary)
    print (json.dumps(dictionary, sort_keys=True, indent=4, separators=(',', ': ')))
    #Результат печати словаря в формате JSON данных
    # {
        #"academic title": "class=person-appointment-title",
        #"fio": "class=b",
        #"photo": "hse.ru/pubs/share/direct/138568616",
        #"post": "class=person-appointment-title"
    # }
    # Почему то значения ключей печатаются не само значение поля, например как с ФИО, а печатается только имя класса, где находится?
    # Итак со всеми нужными нам полями
    elements_json = json.loads(json_data)
    print elements_json["post"]#доступ по ключу
    #class=person-appointment-title
    return json_data


if __name__ == '__main__':
    main()