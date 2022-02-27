def func(num,list):
	try:
		for i in list:
			if type(i) is int:
				if i==num:
					return str(list.index(i))
		else:
			return str(list.index(i))+">"+ func(num,i)
	except:
		return 0
		
		
lis=[[1,2,3,4],[5,6,7,8,9]]
a=func(11,lis)
print(a)