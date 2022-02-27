file = open("books.txt", "r")

#your code goes here
content=file.readlines()

y=len(content)
for i in range(y):
    a=content[i]
    b=a[0]
    if i==y-1:
        print(b+str(len(a)))
    else:
        print(b+str(len(a)-1))
        
file.close()