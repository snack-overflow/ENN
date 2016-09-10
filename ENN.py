import sqlite3
conn = sqlite3.connect('top1000.db')
import pickle
import math
import test



def getClassStatistics(movie="",k=100):
    stats = [0 for x in range(5)]
    n = [0 for x in range(5)]
    c = conn.cursor()
    q_str = "select user_id,review from reviews where movie_id ="+movie + "order by review"
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


conn.close()
