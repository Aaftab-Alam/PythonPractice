list=["s","w","g"]

i=0
points=0

while i<=5:
	import random
	comp=random.choice(list)
	#print(comp)
	
	user=input("Choose one\ns for Snake\nw for Water\ng for Gun\n")
	
	if (comp=="s" and user=="g") or (comp=="w" and user=="s") or (comp=="g" and user=="w"):
		
		print("\nYOU WON!")
		
		points+=1
	
	elif(comp==user):
		print("\nTie!")
	
	#elif(user != "w" or "g" or "s"):
	#	print("\nInvalid input")
		
	else:
		print("\nYOU LOOSE")
	
	print(f"Your current point is {points}")
	print(f"Computer input was {comp}\n\n")
	i=i+1
print(f"Your total point is {points}")