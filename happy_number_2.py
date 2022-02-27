#this code will print all the happy numbers in given range
n=int(input("Number"))
for i in range(10,n):
#	num1=i
	num=i#int(input("Enter a number"))
	def func(num):
			str_num=str(num)
			list=[]
			for k in str_num:
				list.append(int(k))
				sum=0
			for j in list:
			    sum=sum+j**2
			if sum==1:
			    	print(i ,"Number is Happy")
			else:
			 #   print(sum)
			    num=sum
			    func(num)
	try:
		func(num)
	except:
		print(num,"Number is not happy")		    
			    	
		