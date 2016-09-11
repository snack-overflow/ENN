import time
import sqlite3
import os
import pickle
import math
conn = sqlite3.connect('top500.db')
c=conn.cursor()
c.execute('select user_id,movie_id,review from reviews limit 100')
#500,1000,5000 db
#50,100,250,500

results=c.fetchall()
for i in range(len(results)):
    results[i]=list(results[i])


for i in results:
    os.system("python test.py 500 "+str(i[0])+" "+str(i[1])+" 50 "+str(i[2]))
for i in results:
    os.system("python test.py 1000 "+str(i[0])+" "+str(i[1])+" 50 "+str(i[2]))
for i in results:
    os.system("python test.py 5000 "+str(i[0])+" "+str(i[1])+" 50 "+str(i[2]))

for i in results:
    os.system("python test.py 500 "+str(i[0])+" "+str(i[1])+" 100 "+str(i[2]))
for i in results:
    os.system("python test.py 1000 "+str(i[0])+" "+str(i[1])+" 100 "+str(i[2]))
for i in results:
    os.system("python test.py 5000 "+str(i[0])+" "+str(i[1])+" 100 "+str(i[2]))

for i in results:
    os.system("python test.py 500 "+str(i[0])+" "+str(i[1])+" 250 "+str(i[2]))
for i in results:
    os.system("python test.py 1000 "+str(i[0])+" "+str(i[1])+" 250 "+str(i[2]))
for i in results:
    os.system("python test.py 5000 "+str(i[0])+" "+str(i[1])+" 250 "+str(i[2]))

for i in results:
    os.system("python test.py 500 "+str(i[0])+" "+str(i[1])+" 500 "+str(i[2]))
for i in results:
    os.system("python test.py 1000 "+str(i[0])+" "+str(i[1])+" 500 "+str(i[2]))
for i in results:
    os.system("python test.py 5000 "+str(i[0])+" "+str(i[1])+" 500 "+str(i[2]))