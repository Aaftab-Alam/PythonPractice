from datetime import date
today=date.today()

m= 2020
print("Please Enter Your Name:")
name= input()
print("Please enter your age:")
age=int(input())
print("Enter the number of times u want to print the result")
result=int(input())
n=int(today.year)+100-age
i=0
for i in range(result):
	print(name, "You will be 100 in year", n)
	i=i+1