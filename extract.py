import numpy as N 
def makearrays(dataloc):
	dataloc = "Data/training_set/"
	from time import mktime
	nummovies = 17770
	numusers = 480189
	numratings = 100480507
	
	movieratings = N.zeros(numratings, dtype=N.int8)
	movieids = N.zeros(numratings, dtype=N.int16)
	userids = N.zeros(numratings, dtype=N.int32)
	dates = N.zeros(numratings, dtype=N.int32)
	counter = 0
	
	for i in range(2):
		if i % 100 == 0: print('Extracting movie %d' % i)
		f = open(dataloc + 'mv_%07d.txt' % (i+1), 'rt')
		data = f.readlines()
		f.close()
		print len(data[0])
		

makearrays("")