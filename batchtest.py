import time
start_time = time.time()
import sqlite3

import pickle
import math
conn = sqlite3.connect('top500.db')
c=conn.cursor()
c.execute('select user_id,movie_id,review from reviews limit 100')

def testAll (db='')
    conn = sqlite3.connect(db)
    