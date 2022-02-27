class Person:
	def __init__(self,name,age,gender):
		self.name=name
		self.age=age
		self.gender=gender
		
		
class Publish:
		def __init__(self,publish_content):
			self.publish_content=publish_content
			
		def display(self):
			print("Content of Publishing:-",self.publish_content)
		
						
class Faculty(Person):
	def __init__(self,name,age,gender,role,content):
		super().__init__(name,age,gender)
		self.role=role
		self.content=Publish(content)
		
	def display(self):
		print("Name :",self.name)
		print("Age :",self.age)
		print("Gender :",self.gender)
		print("Role :",self.role)
		self.content.display()
		
		
obj=Faculty("Aadil",18,"male","student","This is content")
obj.display()