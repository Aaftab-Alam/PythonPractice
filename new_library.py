class Librarian:
	def __init__(self,name,number):
		self.name=name
		self.number=number
		print("1.Check books\n2.Add books\n3.Customer infor")
		decision=input()
		
		def check_books(self):
			with open (str(self.name)+"books.txt","r") as books:
				print(books.read())
				
		def customer_info(self):
			with open(str(self.name)+"customer_info.txt","r") as customer:
				print(customer.read())
		
		def add_books(self):
			with open(str(self.name)+"books.txt","a") as books_write:
				inp=input("Enter books name separated by commas").split(",")
				books_write.write(inp)
				
		
obj=Librarian("Aadil",7052891316)