import sqlite3
import pickle
import csv
import pandas
import math
conn = sqlite3.connect("top500.db")


def getCorrelation(user_i="",user_j=""):
   c= conn.cursor()
   c.execute("SELECT A.movie_id ,A.user_id `A_user`, B.user_id `B_user`, A.time `A_time`, B.time `B_time`, A.review `A_review`, B.review `B_review` from (select * from reviews where user_id="+str(user_i)+") as A join (select * from reviews where user_id="+str(user_j)+") as B on A.movie_id=B.movie_id")
   all_results = c.fetchall()
   conn.commit()
   #print all_results
   avg_ratings = pickle.load(open("user_avg_rating","rb"))
   mu_i = avg_ratings[int(user_i)]
   mu_j = avg_ratings[int(user_j)]
   M = len(all_results)
   sigma_i =0
   sigma_j = 0
   E = 0
   for row in all_results:
       del_t = -abs(row[3]-row[4])
       E += (row[5] - mu_i) * (row[6] - mu_j)*math.exp(del_t/495)
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





def saveAllCorrelation():
    with open("top_500_users","rb") as f:
        all_users = pickle.load(f)
    file = open("allCorrelations.csv","a+b")
    writer = csv.writer(file)
    user=[]
    for i in range(198,len(all_users)):
        user.append(list(all_users[i])[0])
    for i in range(198,len(all_users)):
        for j in range(i + 1,len(all_users)):
            print i,j
            corr = getCorrelation(user[i],list(all_users[j])[0])
            writer.writerow([user[i],list(all_users[j])[0],corr])

    file.close()


# def csvToDict():
#     my_dict = {}
#     with open("test_data.csv","rb") as file:
#         reader = pandas.read_csv(file)

#     for i in range(len(reader)):
#         my_dict[str(row[0][i]) +"-"+ str(row[1][i])] = row[2][i]
#     pickle.dump(my_dict,open("allCorrelations","wb")
saveAllCorrelation()
conn.close()

