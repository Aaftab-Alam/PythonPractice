def mergesort(lis):
	if len(lis)>1:
		mid=len(lis)//2
		lefthalf=lis[:mid]
		righthalf=lis[mid:]
		mergesort(lefthalf)
		mergesort(righthalf)
		
		i=j=k=0
		while i<len(lefthalf) and j<len(righthalf):
			if lefthalf[i]<righthalf[j]:
				lis[k]=lefthalf[i]
				i+=1
				k+=1
			else:
				lis[k]=righthalf[j]
				j+=1
				k+=1
		while i<len(lefthalf):
			lis[k]=lefthalf[i]
			i=i+1
			k=k+1
		while j<len(righthalf):
			lis[k]=righthalf[j]
			j=j+1
			k=k+1

import random
lest=[]
for i in range(1,1000):
	ran=random.randint(1,5000)
	lest.append(ran)
lest2=lest
import time
#start2=time.time()
#lest2.sort
#end2=time.time()
#print((end2-start2)*1000)

start=time.time()
mergesort(lest)
end=time.time()
print(lest)
print((end-start)*1000)

def binary_search(list,x,low, high):

  while low<=high :
    mid=(low+ high)//2
    if list[mid]==x:
      return mid

    elif list[mid]<x:
      low=mid+1
    else:         # x<list[mid]
      high=mid-1
  return -1


#arr=input("Enter the list of  nos in sorted order: ")
#arr=arr.split()
#arr=[int(x) for x in arr]
key=int(input("enter the number you want to search :"))
search_start=time.time()
z=binary_search(lest,key,0,len(lest)-1) # z=-1 z!=-1

if (z==-1):
  print("not found")
else:
  print(" Found at index", z)
search_end=time.time() 
print((search_end-search_start)*1000)

#def binary__search(list,x):
#	if (low==high-1):
#		return -1
#	else:
#		mid=low+high//2
#		print(mid)
#		if list[mid]==x:
#			return mid
#		elif list[mid]<x:
#			binary__search(list,x,mid+1,high)
#		else:
#			binary__search(list,x,low,mid)
#	else:
#		#	return -1
#aadil=time.time()
#a=binary__search(lest,key,0,len(lest)-1)
#if a==-1:
#		print("Not found")
#else:
#		print("Found at",a)
#aaftab=time.time()
#print((aaftab-aadil)*1000)
#		