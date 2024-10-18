from boobleSort import boobleSort
from selectionSort import selectionSort
import numpy as np
	
def bucketSort(lista):
	bucket1=np.array([])
	bucket2=np.array([])
	bucket3=np.array([])
	bucket4=np.array([])
	listaFinal=np.array([])
	for elemento in lista:
		if elemento <25:
			bucket1=np.append(bucket1,elemento)

		elif elemento >=25 and elemento <50:
			bucket2=np.append(bucket2,elemento)
	
		elif elemento >=50 and elemento <75:
			bucket3=np.append(bucket3,elemento)
	
		else :
			bucket4=np.append(bucket4,elemento)
	if bucket1.size>0:
		bucket1=selectionSort(bucket1)
	if bucket2.size>0:
		bucket2=selectionSort(bucket2)
	if bucket3.size>0:
		bucket3=selectionSort(bucket3)
	if bucket4.size>0:
		bucket4=selectionSort(bucket4)
	
	listaFinal=np.concatenate((listaFinal,bucket1,bucket2,bucket3,bucket4))
	return listaFinal
	
	
	


lista=np.random.randint(0,100,8)
print(lista)
lista=bucketSort(lista)
print(lista)
