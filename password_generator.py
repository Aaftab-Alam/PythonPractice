import random
import string
import time
initial=time.time()
i=0
while True:
	inp=int(input("Length of password:"))
	inp1=input("Strength of the password strong/weak?:")
	#print(inp)
	
	def func_string():
		if inp1=="weak":
			weak=''.join(random.choices(string.ascii_uppercase + string.digits , k=inp ))
			return weak
			
		elif inp1=="strong":
			strong=''.join(random.choices(string.ascii_letters + string.digits + string.punctuation , k=inp ))
			return strong
		
		else:
			return "Invalid Syntax"
	
	print(func_string()+ "\n")

	inp3=input(("You want to generate password Again? Yes\\no\n"))
	if inp3=="yes":
		pass
	elif inp3=="no":
		exec=time.time()
		print(f"Program executed in {(exec-initial)} seconds")
		break
	else:
		print("Invalid syntax\nTry again")
		
	i=i+1