num=int(input("number"))
start=1
a=0
list=[]
for i in range(num):
	a+=start
	if a>=num:
		break
	else:
		pass
	for i in range(0,1):
	#	sum=a+start
		start+=a
		list.append(a)
		list.append(start)
		print(a , "+", start, "+" , end=" ")

	#	print(a+start)
from functools import reduce

num1=reduce(lambda x,y:x+y , list)
print("\n"+str(num1))