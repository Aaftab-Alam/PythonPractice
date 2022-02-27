n= int(input("Num"))

#Question1
for i in range(1,n+1):
	for j in range(1,i+1):
		print("*",end=" ")
	print("")
	
print("\n[Program finished]\n")

#Question2
for i in range(1,n+1):
	for j in range(i,0,-1):
		print(j,end=" ")
	for k in range(2,i+1):
		print(k,end=" ")
	print("")
		
print("\n[Program finished]\n")

#Question4
for i in range(1,n+1):
	for j in range(n,i,-1):
		print(" ",end=" ")
	for k in range(1,i+1):
		print(k,end=" ")
	for l in range(i-1,0,-1):
		print(l,end=" ")
	print("")

print("\n[Program finished]\n")

#DiamondPattern
for i in range(1,n+1):
	for j in range(n,i,-1):
		print(" ",end="")
	for k in range(1,i+1):
		print("*",end="")
	for l in range(1,i):
		print("*",end="")
	print("")
for i in range(1,n):
	for j in range(1,i+1):
		print(" ",end="")
	for k in range(n,i,-1):
		print("*",end="")
	for l in range(n,i+1,-1):
		print("*",end="")
	print("")
	
print("\n[Program finished]\n")

#Question3
for i in range(1,n+1):
	for j in range(1,n+1):
		if i==1 or j==1 or i==n or j==n:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print("")
	
print("\n[Program finished]\n")

#Question5
for i in range(1,n+1):
	for j in range(1,i+1):
		print(i,end=" ")
	print(" ")
	
print("\n[Program finished]\n")
	
#EmptyUpsideDownTriangle
for i in range(1,n+1):
	for j in range(1,n+1):
		if i==1 or j==i:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	for k in range(1,n):
		if i==1 or k==(n-i):
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print("")

#for i in range(1,n+1):
#	for j in range(n,i,-1):
#		print(" ",end="")
#	x=str(11**(i-1))
#	y=[print(i,end=" ") for i in x]
#	print("")
		