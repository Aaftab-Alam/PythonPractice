def partition(a,p,r):
	pivot=a[r]
	i=p
	j=r-1
	
	while i<=j:
		while(a[i]<pivot):
			i+=1
		while (a[j]>pivot):
			j-=1

		if i<j:
			a[i],a[j]=a[j],a[i]
			i+=1
			j-=1

	a[i],a[r]=a[r],a[i]
	return i

def Quick_sort(a,p,r):
	if p<r:
		q=partition(a,p,r)
		Quick_sort(a,p,q-1)
		Quick_sort(a,q+1,r)


data = [24,9,19,14,29,27]
print("Unsorted Array")
print(data)

size = len(data)

Quick_sort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)