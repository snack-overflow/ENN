import sqlite3
#conn = sqlite3.connect('top1000.db')
import pickle
import math
#import test
import csv
import pandas
import exec_db

def getUserReviewClasses(movie_id=''):
    class_1=[]
    class_1=execQuery(query="select distinct user_id from reviews where review=1 and movie_id="+str(movie_id),dB= "top500.db")
    for i in range(len(class_1)):
        class_1[i]=list(class_1[i])[0]


    class_2=[]
    class_2=execQuery(query="select distinct user_id from reviews where review=2 and movie_id="+str(movie_id),dB= "top500.db")
    for i in range(len(class_2)):
        class_2[i]=list(class_2[i])[0]


    class_3=[]
    class_3=execQuery(query="select distinct user_id from reviews where review=3 and movie_id="+str(movie_id),dB= "top500.db")
    for i in range(len(class_3)):
        class_3[i]=list(class_3[i])[0]


    class_4=[]
    class_4=execQuery(query="select distinct user_id from reviews where review=4 and movie_id="+str(movie_id),dB= "top500.db")
    for i in range(len(class_4)):
        class_4[i]=list(class_4[i])[0]

    class_5=[]
    class_5=execQuery(query="select distinct user_id from reviews where review=5 and movie_id="+str(movie_id),dB= "top500.db")
    for i in range(len(class_5)):
        class_5[i]=list(class_5[i])[0]

def getClassStatistics(user="",movie="",k=100):
    stats = [0 for x in range(5)]
    n = [0 for x in range(5)]
    c = conn.cursor()
    q_str = "select user_id,review from reviews where movie_id ="+movie + "and user_id not in" order by review"
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

#conn.close()
