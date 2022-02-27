class BookFile:
	def display(self):
		print(self.librarian_name)
	
	def file_exist(self):
			try:
				with open(str(self.librarian_name)+"books.txt","x"):
					pass
			except:
				pass
	

	def open_book_file(self,call_func,book=None):
		with open(str(self.librarian_name)+"books.txt","r+") as books:
				
				def add_book(add_return):
					if add_return=="add":
						inp=input("Enter books name separated by commas :").split(",")
						
						for name in inp:
							books.write(name+"\n")
						status="added"
					elif add_return=="return":
						inp=input("Enter book name :")
						books.write(name+"\n")
						status="returned"
					else:
						pass
						
					print(f"Books {status} successfully!")
				
				def check_books():
					books_read=books.read()
					if len(books_read)==0:
						print("No books available currently")
					else:
						print(books_read)
						
				def  lend_book():
					read_name=books.readlines()
					if (book_name+"\n") in read_name:
						names.seek(0)
			
						for i in read_name:
							if i!=(book_name+"\n"):
								names.write(i)
							names.truncate()
						print("Book issued successfully")
					
					else:
						print("This book is not available in our library currently.")
						
				
				if call_func=="1a":
				 	add_book("add")
				 
				 
class CustomerFile:
		def open_customer_file(self,call_func):
				with open(str(self.librarian_name)+"customer_info.txt","r+") as cstmr:
					def view_cstmr():
							print(cstmr.read())	
					
					def cstmr_addbook(self,lar):
							status=lar
							cstmr.write(f"Book name:-{book_name} :\n{status}:-\nCustomer name:-{self.name}\nCustomer Address:-{self.address}\nCustomer phone number:-{self.phonenumber}\n\n")
			
						#	print("Books {status} successfully!")
						
class Librarian(BookFile,CustomerFile):
		def __init__(self,name,number):
				self.librarian_name=name
				self.librarian_number=number
			#	self.choice=input("'Choice")
				print("1.Add Book")
				print("2.Check Books")
				print("3.Customer Info")
				self.choice=input()
				
			
				
class Customer(BookFile,CustomerFile):
			def __init_(self,name,number,address):
				self.name=name
				self.phonenumber=number
				self.address=address

print("1.Librarian\n2.Customer")
choice=input()
if choice=="1":
		name=input("Enter your name :")
		number=input("Enter your phonenumber")
		lib_obj=Librarian(name,number)
		lib_obj.file_exist()

if lib_obj.choice=="1":
					lib_obj.open_book_file("1a")
					
						
												
#		
#name=input("Name")
#number=input("Number")
#obj=Librarian(name,number)
#if obj.choice=="1":
#					obj.display()						

#print(BookFile.open_book_file.__dict__)
	

		