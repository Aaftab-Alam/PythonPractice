#####Palindrome######

n=int(input("Num"))
temp=n
sum=0
while n>0:
	r=n%10
	sum=sum*10+r
	n=n//10
if sum==temp:
	print("Number is Palindrome")
else:
	print("Number is not Palindrome")
	
########Armstrong#######

n=int(input("Num"))
temp=n
sum=0
while n>0:
	r=n%10
	sum=sum+r**3
	n=n//10
if sum==temp:
	print("Number is Armstrong")
else:
	print("Number is not Armstrong")
	