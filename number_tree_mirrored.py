n=int(input("Range"))
for i in range(1,n):
	for k in range(1,n-i):
		print(" " , end= " ")
	for j in range(1,i+1):
		print(j ,end =" ")
	for m in range(j-1, 0 ,-1):
		print(m , end=" ")
	print("")