import numpy as np


def selectionSortCurrent(lista,index,indexCurrent,indexMenor):
	if indexCurrent>=np.size(lista):	
		aux=lista[indexMenor]	
		lista[indexMenor]=lista[index]
		lista[index]=aux
		return lista
	if lista[indexCurrent]<lista[indexMenor]:
		indexMenor=indexCurrent
	indexCurrent+=1
	return selectionSortCurrent(lista,index,indexCurrent,indexMenor)
	




def selectionSort(lista,index):
	if index==np.size(lista)-1:
		return lista
	lista=selectionSortCurrent(lista,index,index+1,index)
	index+=1
	return selectionSort(lista,index)





lista=np.random.randint(0,100,10)
print(lista)
selectionSort(lista,0)
print(lista)
