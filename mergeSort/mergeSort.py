import numpy as np

	

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

#lista=np.random.randint(0,100,8)
lista=np.random.randint(0,200,15)
print(str(np.size(lista)))
#mid=np.size(lista)//2
#mid-=1
#merge(lista,mid,nd.size(lista)-1)
lista=mergeAll(lista)
print(lista)



