import time
import sys
import sqlite3
conn = sqlite3.connect('top'+sys.argv[1]+'.db')
import pickle
import math
import csv

# c= conn.cursor()
# c.execute("CREATE TABLE REVIEWS (movie_id integer, user_id integer, review integer, time real);")
# # conn.commit()
# c=conn.cursor()
# c.execute("SELECT user_id,count(review) FROM REVIEWS GROUP BY user_id")
# my_results = sorted(c.fetchall(),key=lambda x: -x[1])
# new_list = my_results[:5000]

# with open("top_5000_users", 'wb') as f:
#     pickle.dump(new_list, f)
# for num in range(len(my_result)):
#         for value in my_result[num]:
#             print str(value) + "   "
#         print
# conn.commit()

def getRMSE(list1,list2):
    error=0
    for i in range(len(list1)):
        error+=math.pow(list1[i]-list2[i],2)
    error=error/len(list1)
    error=math.sqrt(error)        
    return error





def getCorrelation(user_i="",user_j=""):
   c= conn.cursor()
   c.execute("SELECT A.movie_id ,A.user_id `A_user`, B.user_id `B_user`, A.time `A_time`, B.time `B_time`, A.review `A_review`, B.review `B_review` from (select * from reviews where user_id="+str(user_i)+") as A join (select * from reviews where user_id="+str(user_j)+") as B on A.movie_id=B.movie_id")
   all_results = c.fetchall()
   conn.commit()
   #print all_results
   avg_ratings = pickle.load(open("float_avg_user_rating","rb"))
   mu_i = avg_ratings[int(user_i)]
   mu_j = avg_ratings[int(user_j)]
   M = len(all_results)
   sigma_i =0
   sigma_j = 0
   E = 0
   for row in all_results:
       del_t = -abs(row[3]-row[4])
       E += (row[5] - mu_i) * (row[6] - mu_j)*math.exp(del_t/4959393420)
       sigma_i += math.pow((row[5] - mu_i),2)
       sigma_j += math.pow((row[6] - mu_j),2)
   E/=M
   sigma_i/=M
   sigma_j/=M
   sigma_i = math.sqrt(sigma_i)
   sigma_j = math.sqrt(sigma_j)
   correlation = E/(sigma_i*sigma_j)
   beta = 495
   gamma = -2.47
   #correlation += gamma
   return correlation

    #print avg_i,avg_j



def getNearestNeighbours(user_i="",movie="",k=100):
    
    c= conn.cursor()
    c.execute("select user_id, review from REVIEWS where movie_id="+str(movie))
    all_results = c.fetchall()
    
    
    for i in range(len(all_results)):
        all_results[i]=list(all_results[i])
    correlation=[]
    
    for i in range(len(all_results)):
        correlation.append(getCorrelation(user_i,all_results[i][0]))
        all_results[i].append(correlation[i])
    all_results.sort(key=lambda x:-x[2])
    if(k>len(all_results)):
        k=len(all_results)
    return all_results[:k]

def getRatingByKnn(user="",movie="",k=0):

    all_results = getNearestNeighbours(user,movie,k)
    rating = 0
    num = 0
    den = 0
    avg_ratings = pickle.load(open("user_avg_rating","rb"))
    for row in all_results:
        num += row[2]*(row[1]-avg_ratings[int(row[0])])
        den += abs(row[2])
    rating = num/den + avg_ratings[int(user)]
    return rating



rating=getRatingByKnn(sys.argv[2],sys.argv[3],int(sys.argv[4]))
#user movie predicted actual db k
#obj = [int(sys.argv[2]), int(sys.argv[3]),  float(str(rating)),float(str(sys.argv[5])), int(sys.argv[1]) ]

conn.close()
#getCorrelation("387418","305344")
 

with open("test_data.csv", "a+b") as f:
    writer = csv.writer(f)
    writer.writerow([int(sys.argv[2]), int(sys.argv[3]),  float(str(rating)),float(str(sys.argv[5])), int(sys.argv[1]),int(sys.argv[4]) ])

print [int(sys.argv[2]), int(sys.argv[3]),  float(str(rating)),float(str(sys.argv[5])), int(sys.argv[1]),int(sys.argv[4]) ]
