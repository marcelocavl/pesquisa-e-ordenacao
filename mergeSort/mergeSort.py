import numpy as np
import time
import sys

	

def mergeAll(array):	
	if np.size(array)==1:
		return array
	mid=(np.size(array)//2)
	final=np.size(array)
	array[0:mid]=mergeAll(array[0:mid])
	array[mid:final]=mergeAll(array[mid:final])
	return merge(array,mid,final)

def merge(array,mid,final):
	i=0
	j=0
	k=0
	a=array[0:mid]
	b=array[mid:final]
	a=np.append(a,99999)
	b=np.append(b,99999)
	while k<final:
		if a[i]<b[j]:
			array[k]=a[i]
			i+=1
		else: 
			array[k]=b[j]
			j+=1	
		k+=1
	return array

sys.setrecursionlimit(3000)

lista=np.random.randint(0,100000,100000)
print(lista)
inicio=time.time()
lista=mergeAll(lista)
fim=time.time()
print(fim-inicio)
print(lista)



