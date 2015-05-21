# -*- coding: utf-8 -*-
# __author__ = 'Admin'
from scipy import stats

class ParseCSV:

    def readCSV(self, fileName='NLPresults2', ind=[2,3,6,7]):
        f = open(fileName+'.csv','r')
        fd=f.read().decode('utf-8')
        lines = fd.split("\n")

        list_auth_avto=[]
        list_auth_man=[]
        list_topic_avto=[]
        list_topic_man=[]
        j=0
        val=0
        list2=[]
        for line in lines:
            if line == ';;;;;;;;;;;;;;':
                val1=stats.spearmanr(list_auth_avto,list_auth_man) #
                #print list2#list_auth_avto,list_auth_man, val1
                #print stats.spearmanr(list_topic_avto,list_topic_man) #n
                list2.append([list_auth_avto,list_auth_man, list_topic_avto, list_topic_man])
                j=j+1
                val=val+val1[0]
                list_auth_avto=[]
                list_auth_man=[]
                list_topic_avto=[]
                list_topic_man=[]

            cells=line.split(';')
            try:
                #list2=[float(cells[2]),float(cells[3]),float(cells[6]),float(cells[7])]
                list_auth_avto.append(float(cells[ind[0]]))
                list_auth_man.append(float(cells[ind[1]]))
                list_topic_avto.append(float(cells[ind[2]]))
                list_topic_man.append(float(cells[ind[3]]))
            except:
                pass
            #print line, list_auth_avto
        return list2#val/j

    def countPersent(self, _matrix, _num, _marks=set([7,8,9,10])):
        j=0
        for _lists in _matrix:
            i=0
            _list_item=_lists[3]
            try:
                for _mark in range(_num):#_lists[3]len(_list_item)
                    if _list_item[_mark] in _marks:
                        i=1
            except:
                pass
            if i!=0:
                j=j+1
        return 100*j/len(_matrix)

    def countMAP(self, _matrix, _max_num=1):
        _sum=0
        for _num in range(_max_num):
            #print self.countPersent(_matrix, _num)
            _sum=_sum+self.countPersent(_matrix, _num+1)
        return _sum/_max_num


pc=ParseCSV()
matrix= pc.readCSV('NLPresults2')#, [2,3,4,5])
print pc.countPersent(matrix, 10, [6,7,8,9,10])
print pc.countMAP(matrix, 10)