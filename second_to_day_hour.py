seconds=int(input("Enter seconds"))

day=seconds//3600//24
hour=seconds//3600%24
minute=seconds%3600//60
second=seconds%60

print(day, "Day" ,hour,"hour" , minute, "minute" , second, "seconds")