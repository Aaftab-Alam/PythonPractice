num=int(input("Enter a number"))
def func(num):
		str_num=str(num)
		list=[]
		for i in str_num:
			list.append(int(i))
			sum=0
		for j in list:
		    sum=sum+j**2
		if sum==1:
		    	print("Number is Happy")
		else:
		    print(sum)
		    num=sum
		    func(num)
try:
	func(num)
except:
	print("Number is not happy")		    
		    	
	