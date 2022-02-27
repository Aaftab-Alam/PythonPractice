terms = int(input("Number:"))
# first two terms
num1, num2 = 0, 1
#count = 0
temp=0
list=[]
print("Fibonacci sequence:")
while temp <= terms:
    print(temp,"+" ,end=" ")
    temp = num1 + num2
    list.append(temp)
    # update values
    num1 = num2
    num2 = temp
from functools import reduce
sum=reduce(lambda x,y:x+y , list)
print("\nSum:"+str(sum))