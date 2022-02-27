class Vehicle:

	def __init__(self, name, max_speed, mileage):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage
	def info(self):
		return f"Name: {self.name} \nSpeed: {self.max_speed}\nMileage: {self.mileage}"
class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def info(self):
		return f"Name: {self.name}\nAge: {self.age}"
a=Vehicle("SchoolVolvo" , 80 ,12)
c=Vehicle("Bus",90,15)
b=Person("Aadil",18)
print(a.info())
print("\n")
print(c.info())
print("\n")
print(b.info())
