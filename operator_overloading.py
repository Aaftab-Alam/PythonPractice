

class Time:
	def gettime(self):
		self.hour=int(input("Enter hour: "))
		self.minute=int(input("Enter minute: "))
		self.second=int(input("Enter seconds: "))
	
	def display(self):
		print(f"Time is {self.hour}:{self.minute}:{self.second}\n")
		
	def __add__(self,other):
		sum=Time()
		sum.hour=self.hour+other.hour
		sum.minute=self.minute+other.minute
		if sum.minute>=60:
			sum.hour+=1
			sum.minute-=60
		sum.second=self.second+other.second
		if sum.second>=60:
			sum.minute+=1
			sum.second-=60
		
		return sum
		

a=Time()
a.gettime()
a.display()


b=Time()
b.gettime()
b.display()

c=a+b
c.display()