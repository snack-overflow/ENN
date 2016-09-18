import sqlite3
#conn = sqlite3.connect('top1000.db')
import pickle
import math
#import test
import csv
import pandas
from exec_db import *
Faizaan Charania (faizaancharania@gmail.com)

def getUserReviewClasses(movie_id='', user=''):
   class_1=[]
   class_1=execQuery(query="select distinct user_id from reviews where review=1 and movie_id="+str(movie_id)+ " and user_id<>" + str(user),dB= "top500.db")
   for i in range(len(class_1)):
       class_1[i]=list(class_1[i])[0]


   class_2=[]
   class_2=execQuery(query="select user_id from reviews where review=2 and movie_id="+str(movie_id)+ " and user_id<>" + str(user),dB= "top500.db")
   for i in range(len(class_2)):
       class_2[i]=list(class_2[i])[0]


   class_3=[]
   class_3=execQuery(query="select user_id from reviews where review=3 and movie_id="+str(movie_id)+ " and user_id<>" + str(user),dB= "top500.db")
   for i in range(len(class_3)):
       class_3[i]=list(class_3[i])[0]


   class_4=[]
   class_4=execQuery(query="select user_id from reviews where review=4 and movie_id="+str(movie_id)+ " and user_id<>" + str(user),dB= "top500.db")
   for i in range(len(class_4)):
       class_4[i]=list(class_4[i])[0]

   class_5=[]
   class_5=execQuery(query="select user_id from reviews where review=5 and movie_id="+str(movie_id)+ " and user_id<>" + str(user),dB= "top500.db")
   for i in range(len(class_5)):
       class_5[i]=list(class_5[i])[0]

   return class_1,class_2,class_3,class_4,class_5

def getClassStatistics(user="",movie="",k=100):
    stats = [0 for x in range(5)]
    n = [0 for x in range(5)]
    c = conn.cursor()
    q_str = "select user_id,review from reviews where movie_id ="+movie + "and user_id <>"+ user+" order by review"

    c.execute(q_str)
    result = c.fetchall()
    other_users = result
    for user in result:
        n[int(user[1])-1] +=1
        neighbours = getNearestNeighbours(user,movie,k)
        for other in neighbours:
            if user[1] == other[1]:
                stats[int(user[1])-1]+=1
            else:
                pass
    for i in range(len(stats)):
        stats[i]/=k
        stats[i]/=n[i]
    return stats

def getCorrelation(user1='', user2=''):
   with open('allCorrelations.csv','rb') as f:
       all_corr=pandas.read_csv(f,header=None)
       for i in range(len(all_corr)):
           if all_corr.ix[i][0]==int(user1) and all_corr.ix[i][1]==int(user2):
               corr=all_corr.ix[i][2]
           elif all_corr.ix[i][0]==int(user2) and all_corr.ix[i][1]==int(user1):
               corr=all_corr.ix[i][2]
   return corr

def getNearestNeighbours(user=''):
   all_corr=[]
   results=[]
   with open('allCorrelations.csv','rb') as f:
       all_corr=pandas.read_csv(f,header=None)
       for i in range(len(all_corr)):
           if all_corr.ix[i][0]==int(user):
               results.append([ all_corr.ix[i][1], all_corr.ix[i][2]])
           elif all_corr.ix[i][1]==int(user):
                results.append([all_corr.ix[i][0], all_corr.ix[i][2]])
   results.sort(key=lambda x: -x[1])
   return results

def getAllNearestNeighbours(class_1=[], class_2=[], class_3=[], class_4=[], class_5=[],k=50):
   class1_data = []
   class2_data = []
   class3_data = []
   class4_data = []
   class5_data = []
   for i in range(len(class_1)):
       user_dict = {}
       user_dict['user'] = class_1[i]
       del_indexes = []
       allNeighbours = []
       allNeighbours = getNearestNeighbours(class_1[i])
       print allNeighbours, "nnnnnnnnnnnnnnnnnn"
       for i in range(len(allNeighbours)):
           if allNeighbours[i][0] in class_1:
               allNeighbours[i].append(1)
           elif allNeighbours[i][0] in class_2:
               allNeighbours[i].append(2)
           elif allNeighbours[i][0] in class_3:
               allNeighbours[i].append(3)
           elif allNeighbours[i][0] in class_4:
               allNeighbours[i].append(4)
           elif allNeighbours[i][0] in class_5:
               allNeighbours[i].append(5)
           else:
               del_indexes.append(allNeighbours[i])
       for i in del_indexes:
           allNeighbours.remove(i)
       if k< len(allNeighbours):
           user_dict['allNeighbours'] = allNeighbours[:k]
       else:
           user_dict['allNeighbours'] = allNeighbours
       class1_data.append(user_dict)

   for i in range(len(class_2)):
       user_dict = {}
       user_dict['user'] = class_2[i]
       del_indexes = []
       allNeighbours = []
       allNeighbours = getNearestNeighbours(class_2[i])
       for i in range(len(allNeighbours)):
           if allNeighbours[i][0] in class_1:
               allNeighbours[i].append(1)
           elif allNeighbours[i][0] in class_2:
               allNeighbours[i].append(2)
           elif allNeighbours[i][0] in class_3:
               allNeighbours[i].append(3)
           elif allNeighbours[i][0] in class_4:
               allNeighbours[i].append(4)
           elif allNeighbours[i][0] in class_5:
               allNeighbours[i].append(5)
           else:
               del_indexes.append(allNeighbours[i])
       for i in del_indexes:
           allNeighbours.remove(i)
       if k< len(allNeighbours):
           user_dict['allNeighbours'] = allNeighbours[:k]
       else:
           user_dict['allNeighbours'] = allNeighbours
       class2_data.append(user_dict)

   for i in range(len(class_3)):
       user_dict = {}
       user_dict['user'] = class_3[i]
       del_indexes = []
       allNeighbours = []
       allNeighbours = getNearestNeighbours(class_3[i])
       for i in range(len(allNeighbours)):
           if allNeighbours[i][0] in class_1:
               allNeighbours[i].append(1)
           elif allNeighbours[i][0] in class_2:
               allNeighbours[i].append(2)
           elif allNeighbours[i][0] in class_3:
               allNeighbours[i].append(3)
           elif allNeighbours[i][0] in class_4:
               allNeighbours[i].append(4)
           elif allNeighbours[i][0] in class_5:
               allNeighbours[i].append(5)
           else:
               del_indexes.append(allNeighbours[i])
       for i in del_indexes:
           allNeighbours.remove(i)
       if k< len(allNeighbours):
           user_dict['allNeighbours'] = allNeighbours[:k]
       else:
           user_dict['allNeighbours'] = allNeighbours
       class3_data.append(user_dict)
    
    for i in range(len(class_4)):
       user_dict = {}
       user_dict['user'] = class_4[i]
       del_indexes = []
       allNeighbours = []
       allNeighbours = getNearestNeighbours(class_4[i])
       for i in range(len(allNeighbours)):
           if allNeighbours[i][0] in class_1:
               allNeighbours[i].append(1)
           elif allNeighbours[i][0] in class_2:
               allNeighbours[i].append(2)
           elif allNeighbours[i][0] in class_3:
               allNeighbours[i].append(3)
           elif allNeighbours[i][0] in class_4:
               allNeighbours[i].append(4)
           elif allNeighbours[i][0] in class_5:
               allNeighbours[i].append(5)
           else:
               del_indexes.append(allNeighbours[i])
       for i in del_indexes:
           allNeighbours.remove(i)
       if k< len(allNeighbours):
           user_dict['allNeighbours'] = allNeighbours[:k]
       else:
           user_dict['allNeighbours'] = allNeighbours
       class4_data.append(user_dict)

    for i in range(len(class_5)):
       user_dict = {}
       user_dict['user'] = class_5[i]
       del_indexes = []
       allNeighbours = []
       allNeighbours = getNearestNeighbours(class_5[i])
       for i in range(len(allNeighbours)):
           if allNeighbours[i][0] in class_1:
               allNeighbours[i].append(1)
           elif allNeighbours[i][0] in class_2:
               allNeighbours[i].append(2)
           elif allNeighbours[i][0] in class_3:
               allNeighbours[i].append(3)
           elif allNeighbours[i][0] in class_4:
               allNeighbours[i].append(4)
           elif allNeighbours[i][0] in class_5:
               allNeighbours[i].append(5)
           else:
               del_indexes.append(allNeighbours[i])
       for i in del_indexes:
           allNeighbours.remove(i)
       if k< len(allNeighbours):
           user_dict['allNeighbours'] = allNeighbours[:k]
       else:
           user_dict['allNeighbours'] = allNeighbours
       class5_data.append(user_dict)

   return class1_data,class2_data,class3_data,class4_data,class5_data


def getDelN(user,class_user,class1_data=[],class2_data=[],class3_data=[],class4_data=[],class5_data=[]):
    delN=[0,0,0,0,0]
    for i in range(len(class1_data)):
        neighbour=class1_data[i]['allNeighbours'][-1]
        corr=getCorrelation(str(user),str(class1_data[i]['user']))   
        if(corr>neighbour[1]):
            if(class_user==neighbour[2]):
                pass
            else:
                if (neighbour[2]==1):
                    delN[0]-=1
                elif (class_user==1):
                    delN[0]+=1
                else:
                    pass
    for i in range(len(class2_data)):
        neighbour=class2_data[i]['allNeighbours'][-1]
        corr=getCorrelation(str(user),str(class2_data[i]['user']))   
        if(corr>neighbour[1]):
            if(class_user==neighbour[2]):
                pass
            else:
                if (neighbour[2]==2):
                    delN[1]-=1
                elif (class_user==2):
                    delN[1]+=1
                else:
                    pass
    for i in range(len(class3_data)):
        neighbour=class3_data[i]['allNeighbours'][-1]
        corr=getCorrelation(str(user),str(class3_data[i]['user']))   
        if(corr>neighbour[1]):
            if(class_user==neighbour[2]):
                pass
            else:
                if (neighbour[2]==3):
                    delN[2]-=1
                elif (class_user==3):
                    delN[2]+=1
                else:
                    pass
    for i in range(len(class4_data)):
        neighbour=class4_data[i]['allNeighbours'][-1]
        corr=getCorrelation(str(user),str(class4_data[i]['user']))   
        if(corr>neighbour[1]):
            if(class_user==neighbour[2]):
                pass
            else:
                if (neighbour[2]==4):
                    delN[3]-=1
                elif (class_user==4):
                    delN[3]+=1
                else:
                    pass

    for i in range(len(class5_data)):
        neighbour=class5_data[i]['allNeighbours'][-1]
        corr=getCorrelation(str(user),str(class5_data[i]['user']))   
        if(corr>neighbour[1]):
            if(class_user==neighbour[2]):
                pass
            else:
                if (neighbour[2]==5):
                    delN[4]-=1
                elif (class_user==5):
                    delN[4]+=1
                else:
                    pass
def ENN_main(user="", movie="", k= 50):
   class_1,class_2,class_3, class_4, class_5 =  getUserReviewClasses(movie,user)
   print "ALL CLASSES"
   print class_1,class_2,class_3, class_4, class_5
   class1_data,class2_data,class3_data,class4_data,class5_data = getAllNearestNeighbours(class_1,class_2,class_3, class_4, class_5,k)
   print class1_data
   print "1111111111111111111111111111111111111111111"
   print class2_data
   print "2222222222222222222222222222222222222222222"
   print class3_data
   print "3333333333333333333333333333333333333333333"
   print class4_data
   print "4444444444444444444444444444444444444444444"
   print class5_data
   print "5555555555555555555555555555555555555555555"

ENN_main("31254","4",50)