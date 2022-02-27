user=int(input("Please enter a number between 0 to 100\nUser input:"))
a=0
b=100
print("\nComputer has 8 chances to guess the number\n")
import time
i=1
while i<=8:
	import random
	comp=random.randint(a,b)
	print("Computer Guessed:"+ str(comp))
	if comp>user:
		print("Computer should guess a lower number")
		b=comp-1
	elif comp<user:
		print("Computer should guess a higher number")
		a=comp+1
	else:
		print("Computer won!")
		print(f"Computer guessed correctly in {i} chances")
		break
	print(f"Computer has {8-i} chances left\n")
	time.sleep(0.035)
	i=i+1
if comp!=user:
	print("Computer Lost")