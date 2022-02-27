var=input("Enter string")
list=[]
for i in var:
		list.append(i)
			
def func():
	try:	
		for i in range(len(list)):	
			if list[i]==list[i-1]:
				list[i],list[i+1]=list[i+1],list[i]
			else:
				pass
	except:
		pass	
	print(list)

for i in range(len(list)):
			if list[i]==list[i-1]:
				func()
			else:
				pass	
func()

condition=0
for i in range(1,len(list)):
	if list[i]!=list[i-1]:
		condition=0
	else:
		condition=1
		break
		
		
if condition==0:
	var_new=''.join(list)			
	print(var_new)
else:
	print("empty")
	