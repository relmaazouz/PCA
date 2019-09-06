import numpy as np

def list_extract(S):
	list=S.split(" ")
	T=[]
	for s in list:
		if(len(s)>0):
			T.append(float(s))
	
	return T
	
def fileloader(name):

	f=open(name,"r")
	L=f.readlines()
	M=[]
	for line in L:
		if(line!="" and line!="\n"):	M.append(list_extract(line[:len(line)-2]))
	return np.matrix(M)

