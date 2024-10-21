import numpy as np

def substitutionInsertionSort(array,index):
	aux=0
	if index==0:
		return array
	if array[index]<array[index-1]:
		aux=array[index]
		array[index]=array[index-1]
		array[index-1]=aux
	index-=1
	return substitutionInsertionSort(array,index)
		

def insertionSort(array,index,arrayTam):
	if index==arrayTam:
		return	array
	array=substitutionInsertionSort(array,index)
	index+=1
	return insertionSort(array,index,arrayTam)

			
	
	






lista=np.random.randint(0,100,10)

print(lista)
print(np.size(lista))

insertionSort(lista,1,np.size(lista))
print(lista)

