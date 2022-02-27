import random
m=random.randint(1,100)
i=0
while(True):
    print("Please Enter a number:")
    n=int(input())
    i=i+1
    if(i==5):
    	print("You ran out of attempts")
    	print("Number was:",m)
    	break
    if m>n:
    	print("Smaller number. Please try again")
    	print("You have",5-i,"attempts left\n")
    	continue
    elif(m==n):
    	print("You have guessed correctly in", i , "attempt")
    	break
    else:
    	print("Greater number. Please try again")
    	print("You have",5-i,"attempts left\n")
    	continue
    