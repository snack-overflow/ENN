import sqlite3
#conn = sqlite3.connect('top1000.db')
import pickle
import math
#import test
import csv
import pandas
from exec_db import *
# import pdb
# pdb.set_trace()
def getUserReviewClasses(movie_id='', user=''):
   class_1=[]
   class_1=execQuery(query="select distinct user_id from reviews where review=1 and movie_id="+str(movie_id)+ " and user_id<>" + str(user),dB= "top500.db")
   for i in range(len(class_1)):
       #print i, " in for 1 of getUserReviewClasses"
       class_1[i]=list(class_1[i])[0]


   class_2=[]
   class_2=execQuery(query="select user_id from reviews where review=2 and movie_id="+str(movie_id)+ " and user_id<>" + str(user),dB= "top500.db")
   for i in range(len(class_2)):
       #print i, " in for 2 of getUserReviewClasses"
       class_2[i]=list(class_2[i])[0]


   class_3=[]
   class_3=execQuery(query="select user_id from reviews where review=3 and movie_id="+str(movie_id)+ " and user_id<>" + str(user),dB= "top500.db")
   for i in range(len(class_3)):
       #print i, " in for 3 of getUserReviewClasses"
       class_3[i]=list(class_3[i])[0]


   class_4=[]
   class_4=execQuery(query="select user_id from reviews where review=4 and movie_id="+str(movie_id)+ " and user_id<>" + str(user),dB= "top500.db")
   for i in range(len(class_4)):
       #print i, " in for 4 of getUserReviewClasses"
       class_4[i]=list(class_4[i])[0]

   class_5=[]
   class_5=execQuery(query="select user_id from reviews where review=5 and movie_id="+str(movie_id)+ " and user_id<>" + str(user),dB= "top500.db")
   for i in range(len(class_5)):
       #print i, " in for 5 of getUserReviewClasses"
       class_5[i]=list(class_5[i])[0]

   return class_1,class_2,class_3,class_4,class_5



def getCorrelation(user1='', user2=''):
    # print "users ", user1, "   ", user2
    with open('allCorrelations.csv','rb') as f:
        all_corr=pandas.read_csv(f,header=None)
    d = all_corr[((all_corr[0] == int(user1)) & (all_corr[1] == int(user2)))]
    if len(d) < 1:
        d = all_corr[((all_corr[0] == int(user2)) & (all_corr[1] == int(user1)))]
    corr = d.iloc[0][2]
    return corr



def getNearestNeighbours(user=''):
    all_corr=[]
    results=[]
    with open('allCorrelations.csv','rb') as f:
        all_corr=pandas.read_csv(f,header=None)
    d = all_corr[((all_corr[0] == int(user)) | (all_corr[1] == int(user)))]
    all_corr = d
    for i in range(len(all_corr)):
        if all_corr.iloc[i][0]==int(user):
            results.append([all_corr.iloc[i][1], all_corr.iloc[i][2]])
        elif all_corr.iloc[i][1]==int(user):
             results.append([all_corr.iloc[i][0], all_corr.iloc[i][2]])
    results.sort(key=lambda x: -x[1])
    return results

def getAllNearestNeighbours(class_1=[], class_2=[], class_3=[], class_4=[], class_5=[],k=50):
    class1_data = []
    class2_data = []
    class3_data = []
    class4_data = []
    class5_data = []
    for i in range(len(class_1)):
        #print i, " in for 1 of getAllNearestNeighbours"
        user_dict = {}
        user_dict['user'] = class_1[i]
        del_indexes = []
        allNeighbours = []
        allNeighbours = getNearestNeighbours(class_1[i])
        for i in range(len(allNeighbours)):
            #print i, " in for 11 of getAllNearestNeighbours"
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
        #print i, " in for 2 of getAllNearestNeighbours"
        user_dict = {}
        user_dict['user'] = class_2[i]
        del_indexes = []
        allNeighbours = []
        allNeighbours = getNearestNeighbours(class_2[i])
        for i in range(len(allNeighbours)):
            #print i, " in for 22 of getAllNearestNeighbours"
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
        #print i, " in for 3 of getAllNearestNeighbours"
        user_dict = {}
        user_dict['user'] = class_3[i]
        del_indexes = []
        allNeighbours = []
        allNeighbours = getNearestNeighbours(class_3[i])
        for i in range(len(allNeighbours)):
            #print i, " in for 33 of getAllNearestNeighbours"
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
        #print i, " in for 4 of getAllNearestNeighbours"
        user_dict = {}
        user_dict['user'] = class_4[i]
        del_indexes = []
        allNeighbours = []
        allNeighbours = getNearestNeighbours(class_4[i])
        for i in range(len(allNeighbours)):
            #print i, " in for 44 of getAllNearestNeighbours"
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
        #print i, " in for 5 of getAllNearestNeighbours"
        user_dict = {}
        user_dict['user'] = class_5[i]
        del_indexes = []
        allNeighbours = []
        allNeighbours = getNearestNeighbours(class_5[i])
        for i in range(len(allNeighbours)):
            #print i, " in for 55 of getAllNearestNeighbours"
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
        # print i, " in for 1 of getDelN"
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
        # print i, " in for 2 of getDelN"
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
        # print i, " in for 3 of getDelN"
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
        # print i, " in for 4 of getDelN"
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
        # print i, " in for 5 of getDelN"
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
    print delN
    return delN



def getNNOne(user,class_1,class_2,class_3, class_4, class_5):
    all_corr=[]
    results=[]
    class_count=[0,0,0,0,0]
    with open('allCorrelations.csv','rb') as f:
        all_corr=pandas.read_csv(f,header=None)
    d = all_corr[((all_corr[0] == int(user)) | (all_corr[1] == int(user)))]
    all_corr = d
    for i in range(len(all_corr)):
        if i %100 == 99: print i, " in for of getNNOne"
        if all_corr.iloc[i][0]==int(user):
            results.append([all_corr.iloc[i][1], all_corr.iloc[i][2]])
        elif all_corr.iloc[i][1]==int(user):
             results.append([all_corr.iloc[i][0], all_corr.iloc[i][2]])
    results.sort(key=lambda x: -x[1])
    for i in range(len(results)):
        if int(results[i][0]) in class_1:
            class_count[0]+=1
        elif int(results[i][0]) in class_2:
            class_count[1]+=1
        elif int(results[i][0]) in class_3:
            class_count[2]+=1
        elif int(results[i][0]) in class_4:
            class_count[3]+=1
        elif int(results[i][0]) in class_5:
            class_count[4]+=1
    print "class count ", class_count
    return class_count





def getClassStatistics(class1_data = [],class2_data =[],class3_data=[],class4_data=[],class5_data=[],k=100):
    stats = [0 for x in range(5)]
    n = [0 for x in range(5)]

    for i in range(len(class1_data)):
        #print i, " in for 1 of getClassStatistics"
        allNeighbours = class1_data[i]['allNeighbours']
        for neighbour in allNeighbours:
            if neighbour[2] == 1:
                stats[0]+=1.0
    for i in range(len(class2_data)):
        #print i, " in for 2 of getClassStatistics"
        allNeighbours = class2_data[i]['allNeighbours']
        for neighbour in allNeighbours:
            if neighbour[2] == 2:
                stats[1]+=1.0
    for i in range(len(class3_data)):
        #print i, " in for 3 of getClassStatistics"
        allNeighbours = class3_data[i]['allNeighbours']
        for neighbour in allNeighbours:
            if neighbour[2] == 3:
                stats[2]+=1.0
    for i in range(len(class4_data)):
        #print i, " in for 4 of getClassStatistics"
        allNeighbours = class4_data[i]['allNeighbours']
        for neighbour in allNeighbours:
            if neighbour[2] == 4:
                stats[3]+=1.0
    for i in range(len(class5_data)):
        #print i, " in for 5 of getClassStatistics"
        allNeighbours = class5_data[i]['allNeighbours']
        for neighbour in allNeighbours:
            if neighbour[2] == 5:
                stats[4]+=1.0

    n[0] = len(class1_data)
    n[1] = len(class2_data)
    n[2] = len(class3_data)
    n[3] = len(class4_data)
    n[4] = len(class5_data)
    for i in range(len(stats)):
        #print i, " in for last of getClassStatistics"
        stats[i]/=k
        if(n[i]==0):
            stats[i]=0
        else:
            stats[i]/=n[i]
    return stats


def ENN_main(user="", movie="", k= 100):
    # class_1,class_2,class_3, class_4, class_5 =  getUserReviewClasses(movie,user)
    # with open("class_1","wb") as file:
    #     pickle.dump(class_1,file)
    # with open("class_2","wb") as file:
    #     pickle.dump(class_2,file)
    # with open("class_3","wb") as file:
    #     pickle.dump(class_3,file)
    # with open("class_4","wb") as file:
    #     pickle.dump(class_4,file)
    # with open("class_5","wb") as file:
    #     pickle.dump(class_5,file)

    # class1_data,class2_data,class3_data,class4_data,class5_data = getAllNearestNeighbours(class_1,class_2,class_3, class_4, class_5,k)
    with open("class1_data","rb") as file:
        class1_data = pickle.load(file)
    with open("class2_data","rb") as file:
        class2_data = pickle.load(file)
    with open("class3_data","rb") as file:
        class3_data = pickle.load(file)
    with open("class4_data","rb") as file:
        class4_data = pickle.load(file)
    with open("class5_data","rb") as file:
        class5_data = pickle.load(file)
    with open("class_1","rb") as file:
        class_1 = pickle.load(file)
    with open("class_2","rb") as file:
        class_2 = pickle.load(file)
    with open("class_3","rb") as file:
        class_3 = pickle.load(file)
    with open("class_4","rb") as file:
        class_4 = pickle.load(file)
    with open("class_5","rb") as file:
        class_5 = pickle.load(file)

    ni=[len(class1_data),len(class2_data),len(class3_data),len(class4_data),len(class5_data)]
    rating_power = [0,0,0,0,0]
    stats=getClassStatistics(class1_data,class2_data,class3_data,class4_data,class5_data,k)
    ki=getNNOne(user,class_1,class_2,class_3,class_4,class_5)
    for j in range(5):
        if stats[j] == 0:
            rating_power[j] = -999
            continue
        temp =0
        delN=getDelN(user,j+1,class1_data,class2_data,class3_data,class4_data,class5_data)
        for i in range(5):
            if(i==j):
                temp+=delN[i]+ki[i]-k*stats[i]
                temp/=((ni[i]+1)*k)
        else:
            temp+=(delN[i]/(ni[i]*k))
        rating_power[j]=temp
    print rating_power
    print "Final rating is ", (rating_power.index(max(rating_power))+1)

ENN_main("2464081","1",50)
