a="word"
list=[]
list1=[]
for i in a:
	list.append(i)
for c in range(len(a)):
	list1=list.copy()
	
	for b in range(len(a)):
		list1.remove(list1[b])
		list1.insert(b, str(c))
		wd=''.join(list1)
		print(wd)
		list1=list.copy()