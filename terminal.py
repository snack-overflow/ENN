import time
import sys
import sqlite3
conn = sqlite3.connect('top500.db')
import pickle
import math


c=conn.cursor()
c.execute('select distinct user_id from reviews where review=1 and movie_id='+str())
class_1=[]
class_1=c.fetchall()

for i in range(len(class_1)):
    class_1[i]=list(class_1[i])[0]
print len(class_1)

c.execute('select distinct user_id from reviews where review=2 and movie_id='+str() ')
class_2=[]
class_2=c.fetchall()

for i in range(len(class_2)):
    class_2[i]=list(class_2[i])[0]
print len(class_2)


c.execute('select distinct user_id from reviews where review=3 and movie_id='+str()')
class_3=[]
class_3=c.fetchall()

for i in range(len(class_3)):
    class_3[i]=list(class_3[i])[0]
print len(class_3)


c.execute('select distinct user_id from reviews where review=4 and movie_id='+str()')
class_4=[]
class_4=c.fetchall()

for i in range(len(class_4)):
    class_4[i]=list(class_4[i])[0]
print len(class_4)

c.execute('select distinct user_id from reviews where review=5 and movie_id='+str()')
class_5=[]
class_5=c.fetchall()

for i in range(len(class_5)):
    class_5[i]=list(class_5[i])[0]
print len(class_5)


conn.close()
