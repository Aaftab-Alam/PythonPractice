class Librarian:
	def __init__(self,name,number):
		self.name=name
		self.number=number
		try:
			with open(str(self.name)+"books.txt","x"):
				pass
		except:
			pass
		try:
			with open(str(self.name)+"customer_info.txt","x"):
				pass
		except:
			pass
			
		
		print("""1.Check books\n2.Add books\n3.Customer info\n4.Clear book records\n5.Clear customer""")
		self.decision=int(input())
		print("\n")
		
	def check_books(self):
			with open (str(self.name)+"books.txt","r") as books:
				books_read=books.read()
				if len(books_read)==0:
					print("No books available currently")
				else:
					print(books_read)
				
	def customer_info(self):
			with open(str(self.name)+"customer_info.txt","r") as customer:
				print(customer.read())
		
	def add_books(self):
			with open(str(self.name)+"books.txt","a") as books_write:
				inp=input("Enter books name separated by commas :").split(",")
				for name in inp:
					books_write.write(name+"\n")
				print("Books added successfully!")
				
	def clear_book(self):
				with open(str(self.name)+"books.txt","r+") as clear:
					clear.truncate()
					
	def clear_customer(self):
				with open(str(self.name)+"customer_info.txt","r+") as clear:
					clear.truncate()
				
				
class Customer:
	def __init__(self,name,address,phonenumber):
		self.name=name
		self.address=address
		self.phonenumber=phonenumber
		
		print("""1.To lend book\n2.To donate book\n3.To return book""")
		self.decision=int(input())
		print("\n")
	
	def lend_book(self):
		book_name=input("Enter book name :")
		librarian=input("Enter Librarian name :")
		with open(str(librarian)+"books.txt","r+") as names:
			read_name=names.readlines()
		#	print(read_name)
		#	print(book_name)
			if (book_name+"\n") in read_name:
				
				with open(str(librarian)+"customer_info.txt","a") as customer_name:
					customer_name.write(f"Book name:-{book_name} :\nIssued to:-\nCustomer name:-{self.name}\nCustomer Address:-{self.address}\nCustomer phone number:-{self.phonenumber}\n\n")
			
				names.seek(0)
			
				for i in read_name:
					if i!=(book_name+"\n"):
						names.write(i)
					names.truncate()
				print("Book issued successfully")
			
			else:
				
				print("This book is not available in our library currently.")
	
	def add_book(self):
			book_name=input("Enter book name :")
			librarian_name=input("Enter librarian name :")
			
			with open(str(librarian_name)+"books.txt","a") as donate:
				donate.write(book_name+"\n")
				
			with open(str(librarian_name)+"customer_info.txt","a") as customer_name:
					customer_name.write(f"Book name:-{book_name} :\nDonated by:-\nCustomer name:-{self.name}\nCustomer Address:-{self.address}\nCustomer phone number:-{self.phonenumber}\n\n")
			
			print("Books donated successfully!")
			
			
def librarian_func():
		name=input("Enter your name :")
		number=input("Enter number :")
		
		lib_obj=Librarian(name,number)
		
		if lib_obj.decision==1:
			lib_obj.check_books()
		elif lib_obj.decision==2:
			lib_obj.add_books()
		elif lib_obj.decision==3:
			lib_obj.customer_info()
		elif lib_obj.decision==4:
			lib_obj.clear_book()
		elif lib_obj.decision==5:
			lib_obj.clear_customer()
		else:
			print("Invalid choice!")
			
def customer_func():
		name=input("Enter your name :")
		address=input("Enter your address :")
		phonenumber=input("Enter your phonenumber :")
		
		customer_obj=Customer(name,address,phonenumber)
		
		if customer_obj.decision==1:
			customer_obj.lend_book()
		elif customer_obj.decision==2:
			customer_obj.add_book()
		else:
			print("Invalid coice")
			
role=int(input("1.For librarian\n2.For customer\n"))
if role==1:
		librarian_func()
elif role==2:
		customer_func()
else:
		print("Invalid Choice.")