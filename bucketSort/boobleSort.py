import numpy as np

def boobleSort(lista):
	i=0
	aux=0
	invercoes=0
	while i+1<=len(lista)-1:
		if lista[i]>lista[i+1]:
			aux=lista[i+1]
			lista[i+1]=lista[i]
			lista[i]=aux
			invercoes+=1
		i+=1
	if invercoes !=0:
		return boobleSort(lista)
	return lista
	


	

	

