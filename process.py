#!/usr/bin/python
#-*- coding:  utf-8 -*-

import sys
from sample import calculateExperts, calculateCategories

def process(mystr): 
  #temp = sys.stdout 
  #sys.stdout = open('log.txt', 'a')
  lenght=10
  expert_dic=calculateExperts(mystr,lenght)
  expert_list=[key for key in expert_dic]
  categ_dic=calculateCategories(mystr,lenght)
  categ_list=[key for key in categ_dic]
  #print expert_list,categ_list
  #sys.stdout.close()                # Вытолкнуть буферы на диск
  #sys.stdout = temp
  return expert_list,categ_list

if __name__ == "__main__":
  process(mystr = """ правосознание стало играть ту роль, которая ему обычно свойственна в развитой правовой системе. Данный тезис подтверждается и изучением взглядов видных советских теоретиков права, которые были приведены выше.""")
  




   
