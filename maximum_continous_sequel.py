list=["flower", "flow","flowes"]
a=min(list ,key=len)

for i in list:
	for j in range(len(a)):
		if a[j]==i[j]:
			pass
		else:
			break
#if last alphabet of a is same then it would not be pr8nted , in order to print that , we must do the code written below		
if j+1==len(a):
	print(a[0:j+1])
else:
	print(a[0:j])