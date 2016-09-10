import pickle
import test
query='delete from reviews where user_id not in ('
with open('top_500_users','rb') as f:
    my_list=pickle.load(f)
for i in range(len(my_list)):
    my_list[i]=list(my_list[i])
    query+=str(my_list[i][0])+','
query=query[:-1]
query+=')'
c=test.conn.cursor()
c.execute(query)
c.execute('select count(*) from reviews')
print c.fetchall()
test.conn.commit()
test.conn.close()