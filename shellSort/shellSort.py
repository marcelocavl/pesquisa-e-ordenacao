import numpy as np
	
def shellSortCmp(lista,index,cmp,gap):
	if cmp<0:
		return lista
	if lista[index]<lista[cmp]:
		aux=lista[cmp]	
		lista[cmp]=lista[index]
		lista[index]=aux
		index=cmp
	cmp=cmp-gap	
	return shellSortCmp(lista,index,cmp,gap)

def shellSortCurrent(lista,index,gap):	
	if index>=np.size(lista):
		return lista
	lista=shellSortCmp(lista,index,index-gap,gap)
	index+=1
	return shellSortCurrent(lista,index,gap)



def shellSort(lista,gap):
	if gap==0:
		return lista	
	lista=shellSortCurrent(lista,0,gap)
	gap=gap//2
	return shellSort(lista,gap)





lista=np.random.randint(0,200,150)
#lista=np.array([3,2,1])
gap=(np.size(lista))//2
print(lista)
shellSort(lista,gap)
print(lista)

