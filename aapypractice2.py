########

str=input("String :  ")
x=[print(i) for i in str if i not in "aeiouAEIOU"]

#########

n=int(input("Number"))
p=int(input("power"))

assert (p>=0) ,"Power can't be negative"
print(n**p)

#########