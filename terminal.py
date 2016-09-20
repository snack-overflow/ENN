import time
import sys
import sqlite3
# conn = sqlite3.connect('top500.db')
import pickle
import math


# c=conn.cursor()
# c.execute('select distinct user_id from reviews where review=1 and movie_id='+str())
# class_1=[]
# class_1=c.fetchall()
#
# for i in range(len(class_1)):
#     class_1[i]=list(class_1[i])[0]
# print len(class_1)
#
# c.execute('select distinct user_id from reviews where review=2 and movie_id='+str() ')
# class_2=[]
# class_2=c.fetchall()
#
# for i in range(len(class_2)):
#     class_2[i]=list(class_2[i])[0]
# print len(class_2)
#
#
# c.execute('select distinct user_id from reviews where review=3 and movie_id='+str()')
# class_3=[]
# class_3=c.fetchall()
#
# for i in range(len(class_3)):
#     class_3[i]=list(class_3[i])[0]
# print len(class_3)
#
#
# c.execute('select distinct user_id from reviews where review=4 and movie_id='+str()')
# class_4=[]
# class_4=c.fetchall()
#
# for i in range(len(class_4)):
#     class_4[i]=list(class_4[i])[0]
# print len(class_4)
#
# c.execute('select distinct user_id from reviews where review=5 and movie_id='+str()')
# class_5=[]
# class_5=c.fetchall()
#
# for i in range(len(class_5)):
#     class_5[i]=list(class_5[i])[0]
# print len(class_5)
#
#
# conn.close()

conn = sqlite3.connect('top500.db')
c=conn.cursor()
c.execute('select user_id,movie_id,review from reviews limit 100')
#500,1000,5000 db
#50,100,250,500

results=c.fetchall()
for i in range(len(results)):
    results[i]=list(results[i])
results.sort(key=lambda x: x[1])

movie1=[]
movie2 = []
movie3 = []
for i in range(len(results)):
    if results[i][1] == 1:
        movie1.append([str(results[i][0]),str(results[i][2])])
    elif results[i][1] == 2:
        movie2.append([str(results[i][0]),str(results[i][2])])
    else:
        movie3.append([str(results[i][0]),str(results[i][2])])


all_movies = []
all_movies.append(["1",movie1])
all_movies.append(["2",movie2])
all_movies.append(["3",movie3])
with open("test_movies","wb") as f:
    pickle.dump(all_movies,f)
conn.close()
