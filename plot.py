import matplotlib.pyplot as plt

plt.plot([50,100,250],[1.03537432844,1.05166534601,1.05546198416],'r',label='top 1000 users')
plt.plot([50,100,250],[1.06583300756,1.06677082825,1.06957935657],'b',label='top 500 users')
plt.legend(loc='best')
plt.xlabel("No. of neighbours (K)")
plt.ylabel("RMSE")
plt.axis([50,255,1.03,1.08])
plt.title("RMSE with integer predictions")
plt.show()
