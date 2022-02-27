posts=[1,2,3,4,5,6,7,8,9,10,11]

num=5
def pagination(page,arr):
	size=len(arr)
	no_of_page=size//num
	if page<=0:
		prev="#"
		next=page+1
		print("posts:",arr[0:num+page*num],"\nPrev:-",prev,"  Next:-",next)	
		
	if page>0 and page<no_of_page:
		prev=page-1
		next=page+1
		print("posts:",arr[page*num:num+page*num],"\nPrev:-",prev,"  Next:-",next)
		
	if page>=no_of_page:
		prev=page-1
		next=no_of_page	
		print("posts:",arr[page*num:size],"\nPrev:-",prev,"  Next:-",next)
		
	return prev,next
	
for i in range((len(posts)//num)+1):
	a,b=pagination(i,posts)
	#print(array[a:b])