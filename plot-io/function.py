import numpy as np

def quadratic (a, b, c):
	n=10
	end=1
	beg=-1

	delta=(end-beg)/(n-1.)

	x = np.zeros(n)
	y = np.zeros(n)
	
	for i in range(n):
		x[i]=beg+i*delta
		print (x)
		y[i]=a*x[i]*x[i] + b*x[i] + c
	return [x,y]
