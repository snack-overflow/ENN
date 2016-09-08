import time
start_time = time.time()
import sqlite3
conn = sqlite3.connect('example.db')
import pickle
import math
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
    print correlation
    return correlation

    #print avg_i,avg_j



def getNearestNeighbours(user_i="",movie="",k=0):
    c= conn.cursor()
    c.execute("select user_id, review from REVIEWS where movie_id="+str(movie))
    all_results = c.fetchall()
    conn.commit()
    for i in range(len(all_results)):
        all_results[i]=list(all_results[i])
    print all_results
    correlation=[]
    for i in range(len(all_results)):
         correlation[i]=getCorrelation(user_i,all_results[i][0])
    print correlation

def get_rating_by_knn(user="",movie="",k=0):

    get_results = getNearestNeighbours(user,movie,k)
    rating = 0
    num = 0
    den = 0
    avg_ratings = pickle.load(open("user_avg_rating","rb"))
    for row in get_results:
        num += row[1]*(row[2]-avg_ratings[int(row[0])])
        den += abs(row[1])
    rating = num/den + avg_ratings[int(user)]




#getCorrelation("387418","305344")
