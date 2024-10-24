import numpy as np


def insertionSortCurrent(lista,index,indexCmp):
	if indexCmp<0:
		return lista
	aux=0
	if lista[index]<lista[indexCmp]:
		aux=lista[index]
		lista[index]=lista[indexCmp]
		lista[indexCmp]=aux	
		index=indexCmp
	indexCmp-=1
	return insertionSortCurrent(lista,index,indexCmp)
	

def insertionSort(lista,index):
	if index>=np.size(lista):
		return lista
	lista=insertionSortCurrent(lista,index,index-1)
	print(lista)
	index+=1
	return insertionSort(lista,index)
	
	
	







lista=np.random.randint(0,100,10)
print(lista)
print("--------------------------------_")
lista=insertionSort(lista,1)
print("--------------------------------_")
print(lista)

