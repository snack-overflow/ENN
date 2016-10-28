import matplotlib.pyplot as plt

plt.plot([50,100,250],[0.995460214907, 1.00133482568,1.00373080872],'r',label='KNN')
plt.plot([50,100,250],[0.97294750198,0.996532801,1.007698237],'b',label='ENN')
plt.legend(loc='best')
plt.xlabel("No. of neighbours (K)")
plt.ylabel("RMSE")
plt.axis([50,250,0.97,1.02])
plt.title("KNN vs ENN (DB: top 500)")
plt.show()
