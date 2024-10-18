import numpy as np

def selectionSort(lista,x=0):
	aux=0
	parcela=lista[x:len(lista)]
	minimo=np.min(parcela)
	aux=parcela[np.argmin(parcela)]
	parcela[np.argmin(parcela)]=parcela[0]
	parcela[0]=aux
	lista[x:len(lista)]=parcela
	if x== len(lista)-2:
		return lista	
	x+=1
	return selectionSort(lista,x)


	
	
	



lista=np.random.randint(0,10,5)
print(lista)
lista=selectionSort(lista)
print(lista)

