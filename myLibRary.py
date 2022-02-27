class Library:
	books_list=[ ]
	books_dict= {}
	
	def __init__(self,name,book):
		self.name=name
		Library.books_list=book
	
	def lend_book(self,name):
		book_name=input("Enter book name")
		
		if book_name in Library.books_list:
			Library.books_dict.update({name:book_name})
			Library.books_list.remove(book_name)
			
			print(Library.books_dict)
			print(Library.books_list)
			
		else:
			print("This book isn't available")
			
	def  donate_book(self,book_name):
		Library.book_list.append(book_name)
		print("Thankyou for donating book")
	
	def return_book(self,name,book_name):
		del Library.books_dict[name]
		
		Library.books_list.append(book_name)
		
		print("Thankyou for using our service")
	
book_list=input("Enter books name :").split(",")

library_object=Library("Thomas",book_list)

print(Library.books_list)

library_object.lend_book("Rdj")
#print(library_object.__dict__)