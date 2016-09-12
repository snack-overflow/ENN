import sqlite3

def execQuery(query="",dB= ""):
    db = sqlite3.connect(dB)
    cursor = db.cursor()
    cursor.execute(query)
    allResults = cursor.fetchall()
    db.close()
    return allResults