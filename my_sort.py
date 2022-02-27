import random
import time
alist=[]

start0=time.time()
alist=[None for i in range(100000)]
end0=time.time()
print(end0-start0)
def my_sort(lis,alist):
	#alist=[]
#	max_num=max(lis)
#	for i in range(max_num):
#		alist.append(None)
		
	for i in lis:
		alist[i-1]=i
	
	result = list(filter(lambda i:i!=None, alist))
	return result


nums=random.sample(range(100000),10)
lis1=nums
lis2=nums

#time using my_sort
start1=time.time()
a=my_sort(lis1,alist)
print(a)
end1=time.time()
print(end1-start1)

#time_using sort
start2=time.time()
lis2.sort()
end2=time.time()

print(end2-start2)
