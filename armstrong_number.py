n=int(input("enter range"))
for a in range(1,n):
	#this counts the number of digits
	digit=0
	temp0=a
	while temp0>0:
		dig=temp0%10
		digit+=1
		temp0=temp0//10
	#this raises the particular digit to the power equal to number of digit	
	sum=0
	temp=a
	while a>0:
		r=a%10
		sum=sum+r**digit
		a=a//10
	if sum==temp:
		print(sum)
	else:
		pass