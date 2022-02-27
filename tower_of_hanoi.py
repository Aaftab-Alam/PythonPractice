def hanoi(n,A,B,C):
	if n>0:
#		print(A,B,C)
		hanoi(n-1,A,C,B)
		
		if A:
			C.append(A.pop())
	#		print(A,B,C)
		hanoi(n-1,B,A,C)
A=[1,2,3,4,5]
C=[]
B=[]
hanoi(len(A),A,B,C)
print(A,B,C)