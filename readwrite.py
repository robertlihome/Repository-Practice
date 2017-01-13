def read():
	f=open("input",'r')
	
	line=f.readline()
	split=line.split()
	a=float(split[2])
	print (a)
	
	line=f.readline()
	split=line.split()
	b=float(split[2])
	print (b)
	
	line=f.readline()
	split=line.split()
	c=float(split[2])
	print (c)

	#clean up 
	f.close()
